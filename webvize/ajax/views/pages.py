from django.utils import simplejson
from django.http import HttpResponse
from cms.models import *
from ajax.forms import *

def create(request):
    data = simplejson.dumps({'success':'NO'})
    return HttpResponse(data, mimetype="application/javascript")


    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            page = form.save()
            data = simplejson.dumps({
                'success':'OK',
                'page':
                {
                'id':page.id,
                'prompt':page.prompt
                }
            })
        else: 
            data = simplejson.dumps({'success':'NO'})
    else: 
        data = simplejson.dumps({'success':'NO'})
    return HttpResponse(data, mimetype="application/javascript")

def delete(request):
    data = simplejson.dumps({'success':'NO'})
    return HttpResponse(data, mimetype="application/javascript")


    if request.method == 'POST':
        form = DeletePageForm(request.POST)
        if form.is_valid():
            page = form.cleaned_data['page']
            page.delete()
            data = simplejson.dumps({ 'success':'OK' })
        else: 
            data = simplejson.dumps({'success':'NO'})
    else: 
        data = simplejson.dumps({'success':'NO'})
    return HttpResponse(data, mimetype="application/javascript")

def edit(request):
    if request.method == 'POST':
        form = ModifyPageForm(request.POST)
        if form.is_valid():
            page = form.cleaned_data['page']
            content = form.cleaned_data['content']
            page.content = content;
            page.save()
            data = simplejson.dumps({ 'success':'OK' })
        else: 
            data = simplejson.dumps({'success':'NO'})
    else: 
        data = simplejson.dumps({'success':'NO'})
    return HttpResponse(data, mimetype="application/javascript")
