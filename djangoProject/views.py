from django.contrib.auth import authenticate, login, get_user_model, logout
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm, RegisterForm


def home_page(request):
    context = {
        'message': 'home page'
    }
    return render(request, 'home_page.html', context)


def about_us_page(request):
    context = {
        'message': 'about us page'
    }
    return render(request, 'about_us_page.html', context)


def contact_us_page(request):
    contact_form = ContactForm()
    if request.method == "POST":
        print(request.POST.get('fullName'))
        print(request.POST.get('email'))
        print(request.POST.get('message'))
    context = {
        'message': 'contact us page',
        'contact_form': contact_form
    }
    return render(request, 'contact_us_page.html', context)


def login_page(request):
    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        username = login_form.cleaned_data.get('userName')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            print('Error')

    context = {
        'message': 'Login Page',
        'login_form': login_form
    }
    return render(request, 'auth/login.html', context)


User = get_user_model()


def register_page(request):
    register_form = RegisterForm(request.POST or None)
    if register_form.is_valid():
        username = register_form.cleaned_data.get('userName')
        email = register_form.cleaned_data.get('email')
        password = register_form.cleaned_data.get('password')
        User.objects.create_user(username=username, email=email, password=password)

    context = {
        'title': 'Register Page',
        'message': 'Register Form',
        'register_form': register_form
    }
    return render(request, 'auth/register.html', context)


def log_out(request):
    logout(request)
    return  redirect('/')
