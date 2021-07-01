from django import forms
from .models import *
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy

class RegistrationForm(forms.ModelForm):
    repeat_password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].required = True
        self.fields['password'].required = True
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    class Meta:
        model = User
        fields = [ 'username', 'password', 'repeat_password', 'email', 'first_name', 'last_name']
        labels = {
            'repeat_password' : gettext_lazy('Repeat Password'),
        }
        widgets = {
            'password' : forms.PasswordInput()
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if(User.objects.filter(email=email).exists()):
            self.add_error('email', 'Email already exists.')
        return email


    # called after specific field cleaning
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        repeated_password = cleaned_data.get('repeat_password')

        if(password != repeated_password):
            self.add_error('password', 'Passwords do not match.')



class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())