from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from accounts.models import CustomUser
from core.models import Photo


class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Перенаправление после успешной регистрации
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'image']


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image']
