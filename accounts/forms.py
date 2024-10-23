from django import forms
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm

from accounts.models import CustomUser
from core.models import Photo


class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'image']


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image']
