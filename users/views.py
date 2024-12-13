from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from users.forms import LoginUserForm, RegisterUserForm, UserPasswordChangeForm, UserProfileForm


# Функция для авторизации
class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {
        'title': 'Авторизация',
    }
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')


# Функция для регистрации
class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    extra_context = {
        'title': 'Регистрация',
    }
    success_url = reverse_lazy('users:login')


# Функция для смены пароля в профиле
class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    template_name = 'users/password_change.html'
    extra_context = {
        'title': 'Смена пароля',
    }
    success_url = reverse_lazy('users:login')


# Функция для отображения профиля
class ProfileView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    extra_context = {
        'title': 'Профиль',
    }

    def get_object(self, queryset = None):
        return self.request.user


