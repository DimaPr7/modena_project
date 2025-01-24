from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import AbstractUser
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.views.generic import DetailView

from .forms import SignUpForm, UserUpdateForm
from django.contrib.auth import get_user_model

from .models import CustomUser

User = get_user_model()


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to a home page after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


class AccountView(DetailView):
    model = CustomUser
    template_name = "account.html"

    def get_object(self, queryset=None):
        return self.request.user


def logout_view(request):
    logout(request)
    return redirect('/')


@login_required
def profile_update(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('account_profile')
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, 'account_update.html', {'form': form})

