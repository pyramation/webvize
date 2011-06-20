from django.shortcuts import render_to_response
from django.template import RequestContext
from cms.models import *

def create(request):
    form = PageForm()
    action = '/pages/create/'
    submit = 'Add Page'
    return render_to_response('pages/create.html', {'form':form, 'action':action, 'submit':submit}, context_instance = RequestContext(request))

def edit(request):
    return render_to_response('pages/edit.html', context_instance = RequestContext(request))

def show(request):
    return render_to_response('pages/show.html', context_instance = RequestContext(request))

def index(request):
    return render_to_response('pages/index.html', context_instance = RequestContext(request))
