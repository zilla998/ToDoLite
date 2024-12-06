from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views
from .views import RegisterUser, ProfileView, UserPasswordChange

app_name = 'users'

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('password_change/', UserPasswordChange.as_view(), name='password_change'),
]