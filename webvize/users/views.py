from django.shortcuts import render_to_response
from django.contrib.auth import authenticate as auth, login as authlogin, logout as authlogout
from django.template import RequestContext
from django.contrib.auth.models import User
from cms.models import *
from users.forms import *

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth(username=username, password=password)
        if user is not None:
            if user.is_active:
                authlogin(request, user)
                return render_to_response('users/login/success.html', context_instance = RequestContext(request))
            else:
                return render_to_response('users/login/disabled.html', context_instance = RequestContext(request))
        else:
            return render_to_response('users/login/invalid.html', context_instance = RequestContext(request))
    return render_to_response('users/login/login.html', context_instance = RequestContext(request))

def logout(request):
    authlogout(request)
    return render_to_response('users/logout.html', context_instance = RequestContext(request))

def forgot(request):
    return render_to_response('users/forgot/form.html', context_instance = RequestContext(request))

def signUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']
            user = User.objects.create_user(username, email, password)
            return render_to_response('users/signup/complete.html', context_instance = RequestContext(request))
    else:
        form = SignUpForm()
    return render_to_response('users/signup/signup.html', {'form':form}, context_instance = RequestContext(request))
