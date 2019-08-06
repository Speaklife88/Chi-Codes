from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
# Log and Reg given to student as foundation for The Wall from Anne & Ciso

def register(request):
    all_users = User.objects.all().values()
    context = {

    }

    print ("register...")
    return render(request, 'lr_app/register.html')

def process(request):
    print ("process...")
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        User.objects.create(
            first_name=request.POST['first-name'],
            last_name=request.POST['last-name'],
            email=request.POST['email'],
            password=request.POST['password']
        )
        last_user_created = User.objects.last()
        request.session['user_id'] = last_user_created.id
        request.session['user_name'] = last_user_created.first_name
        messages.success(request, 'Successfully registered!')
        User.objects.save(using=self._db)
        print ("process works?...")
        return redirect('/success')

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            print ("login???...")
        return redirect('/')
    else:
        user_to_login = User.objects.get(email=request.POST['login-email'])
        request.session['user_id'] = user_to_login.id
        request.session['user_name'] = user_to_login.first_name
        messages.success(request, 'Successfully logged in!')
        print ("login worked????")
        return redirect('/success')

def logout(request):
    request.session.clear()
    return redirect('/')

def success(request):
    if 'user_id' not in request.session:
        print("User not logged in, redirecting................")
        return redirect('/')
    else:
        print ("It IS working...")
        return render(request, 'lr_app/success.html')