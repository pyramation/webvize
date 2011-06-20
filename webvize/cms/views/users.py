from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response
from django.template import RequestContext

def userLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
               login(request, user)
               return render_to_response('users/login/success.html', context_instance = RequestContext(request))
            else:
                return render_to_response('users/login/disabled.html', context_instance = RequestContext(request))
        else:
            return render_to_response('users/login/invalid.html', context_instance = RequestContext(request))
    return render_to_response('users/login/login.html', context_instance = RequestContext(request))

def userForgot(request):
    return render_to_response('users/forgot/form.html', context_instance = RequestContext(request))

def userSignUp(request):
    return render_to_response('users/signup/form.html', context_instance = RequestContext(request))

