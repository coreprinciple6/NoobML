from django.urls import path, include
from . import views

# url patterns to redirect to the correct html page


urlpatterns = [
    # paths common to all users
    path('', views.index, name='index'),

    path('login/', views.login_view, name='login_view'),
    path('register/', views.register_view, name='register_view'),
    path('logged_in/', views.logged_in_view, name='logged_in_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('admin_redirected/', views.admin_redirected_view, name='admin_redirected_view'),

    path('dashboard', views.dashboard_view, name='dashboard_view'),
    path('dashboard/project', views.project_view, name='project_view'),
    path('dashboard/inference', views.inference_view, name='inference_view'),



]