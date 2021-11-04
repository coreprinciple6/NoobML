import csv
import pandas as pd
from django.conf import settings
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render
from django.http import HttpResponse,  HttpResponseRedirect
from .models import *
from django.urls import reverse
from .forms import RegistrationForm, LoginForm, MLForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .train import Feature_engineer


#common view functions

def user_not_admin(user):
    return not user.is_superuser

def user_is_admin(user):
    return user.is_superuser

# should redirect to the very 1st page(homepage) or whatever page u want
def index(request):
   return render(request, 'Home/index.html')

@login_required
@user_passes_test(user_is_admin)
def admin_redirected_view(request):
    # If user is already logged into the website as admin, other user types won't work.
    return HttpResponse('<h1>You are logged in as admin.<br>Logout as admin to log in as a regular user.</h1>')

@login_required
@user_passes_test(user_not_admin, login_url='/Home/admin_redirected')
def logged_in_view(request):
    if(request.user.is_superuser):
        return HttpResponseRedirect(reverse('admin_redirected_view'))
    else:
        return HttpResponseRedirect(reverse('dashboard_view'))


@login_required
@user_passes_test(user_not_admin, login_url='/Home/admin_redirected')
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@user_passes_test(user_not_admin, login_url='/Home/admin_redirected')
def login_view(request):
    if(request.user.is_authenticated):
        return HttpResponseRedirect(reverse('logged_in_view'))
    error_message = None
    if(request.method == 'POST'):

        form = LoginForm(request.POST)
        # form.is_valid() performs validation checks on the data entered by the user
        if(form.is_valid()):
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            # some checks cannot be implemented in the form classes. So we do them here
            if(user is None):
                error_message = "Incorrect username or password."
            else:
                login(request, user)
                return HttpResponseRedirect(reverse('logged_in_view'))
    else:
        # get method indicates user needs to fill in data
        form = LoginForm()
    return render(request, 'Home/login.html', {'form': form, 'error_message': error_message})


def register_view(request):
    if(request.user.is_authenticated):
        return HttpResponseRedirect(reverse('logged_in_view'))
    if(request.method == 'POST'):
        # fill up registration form with data from request dict
        form = RegistrationForm(request.POST)
        if(form.is_valid()):
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()

            return HttpResponseRedirect(reverse('login_view'))
    else:
        form = RegistrationForm()
    return render(request, 'Home/register.html', {'form': form})

#customer specific view functions

def dashboard_view(request):
    return render(request, 'Home/dashboard.html')


@user_passes_test(user_not_admin, login_url='/Home/admin_redirected')
def project_view(request):
    '''
    view that opens ML form where u upload train and test files
    '''
    userid =  request.user
    error_message = None
    if(request.method == 'POST'):
        form = MLForm(request.POST, request.FILES)
        if(form.is_valid()):
            Project = form.save(commit=False)
            Project.U_id = userid
            Project.save()
            return HttpResponseRedirect(reverse('inference_view'))
        else:
            print(' tough luck my guy')
    else:
        # get method indicates user needs to fill in data
        form = MLForm()
    return render(request, 'Home/project.html', {'form': form, 'error_message': error_message})


@user_passes_test(user_not_admin, login_url='/Home/admin_redirected')
def inference_view(request):
    '''
    directs to a page that shows current project with file names and input and target features. From here u can train!
    '''
    if (request.user.is_authenticated):
        try:
            userid = request.user
            project = Project.objects.filter(U_id=userid)

        except(Project.DoesNotExist):
            project = None
        return render(request, 'Home/inference.html', {'project' : project})

def RunModel_view(request, projects_Name):
    '''
    collects current user's project details and sends csv file for feature engineering
    '''
    userid = request.user
    project_deets = Project.objects.get(U_id=userid, Name = projects_Name)
    Train_path = settings.MEDIA_ROOT + str(project_deets.Train_csv)
    Train_data = pd.read_csv(Train_path)

    Test_path = settings.MEDIA_ROOT + str(project_deets.Test_csv)
    Test_data = pd.read_csv(Test_path)
    target = project_deets.Target

    #create instance of Feature_engineer class
    feature_eng = Feature_engineer()
    train_clean = feature_eng.clean(Train_data)
    print(len(train_clean))
    print('checkpoint')