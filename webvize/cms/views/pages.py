from django.shortcuts import render_to_response
from cms.models import *

def create(request):
    form = PageForm()
    action = '/pages/create/'
    submit = 'Add Page'
    return render_to_response('pages/create.html', {'form':form, 'action':action, 'submit':submit})

def edit(request):
    return render_to_response('pages/edit.html')

def show(request):
    return render_to_response('pages/show.html')

def index(request):
    return render_to_response('pages/index.html')
