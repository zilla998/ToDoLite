from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django import forms
from django.contrib.auth import get_user_model


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(max_length=50, label='Логин', widget=forms.TextInput())
    password = forms.CharField(max_length=30, label='Пароль', widget=forms.PasswordInput())


    class Meta:
        model = get_user_model()


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(max_length=50, label='Логин', widget=forms.TextInput())
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput())


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Старый пароль', widget=forms.PasswordInput())
    new_password1 = forms.CharField(label='Новый пароль', widget=forms.PasswordInput())
    new_password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput())


class UserResetPasswordForm(forms.Form):
    pass


class UserProfileForm(forms.ModelForm):
    username = forms.CharField(disabled=True, label='Логин')


    class Meta:
        model = get_user_model()
        fields = ['username']