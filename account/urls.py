from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('register_error', views.register_error, name='register_error'),
    path('login', views.login, name='login'),
    path('login_error', views.login_error, name='login_error'),
    path('logout', views.logout, name='logout')
    ]