from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import User
from django.contrib.auth.decorators import user_passes_test

# Create your views here.

@user_passes_test(lambda u: not u.is_authenticated, login_url='user_recipe_list')
def register(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')

        if name and email and password1 and password2:
            if password1 == password2:
                user = User.objects.create_user(name, email, password1)
                print('User created: ', user)
                print(f"Email: {email}, Password: {password1}")
                return redirect('login')
            else:
                return redirect('register_error')

    return render(request, 'account/register.html')


def register_error(request):
    if request.method == 'POST':
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')

        if password1 != password2:
            return redirect('register_error')

    return render(request, 'account/register_error.html')


@user_passes_test(lambda u: not u.is_authenticated, login_url='user_recipe_list')
def login (request):

    if request.method=='POST':
        email=request.POST.get('email', '')
        password=request.POST.get('password1', '')
        if email and password:
            user=authenticate(request, email=email, password=password)

            if user is not None:
                auth_login(request, user)                 
                print("User logged in:", user)

                return redirect ('user_recipe_list')
            else:
                return redirect ('login_error')
            
    return render (request, 'account/login.html')

def login_error (request):

    if request.method=='POST':
        email=request.POST.get('email', '')
        password=request.POST.get('password1', '')

        if email and password:
            user=authenticate(request, email=email, password=password)

            if user is None:
                auth_login(request, user)
                return redirect ('login_error')
    
    return render (request, 'account/login_error.html')


def logout (request):
    if request.user:
        auth_logout(request)

    return redirect ('/')
