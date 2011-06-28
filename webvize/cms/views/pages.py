from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from cms.models import *

def create(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            page = form.save()
            page.owner = request.user
            page.save()
            return redirect('/pages/%d/' % page.id)
    else:
        form = PageForm()
    action = '/pages/create/'
    submit = 'Add Page'
    return render_to_response('pages/create.html', {'form':form, 'action':action, 'submit':submit}, context_instance = RequestContext(request))

def edit(request, page_id):
    page = get_object_or_404(Page, pk=page_id)
    #form = PageForm(instance=page)
    request.session['page'] = page_id
    return render_to_response('pages/edit.html', {'page':page}, context_instance = RequestContext(request))

def show(request, page_id):
    page = Page.objects.get(pk=page_id)
    return render_to_response('pages/show.html', {'page':page}, context_instance = RequestContext(request))

def index(request):
    pages = Page.objects.all()
    return render_to_response('pages/index.html', {'pages':pages}, context_instance = RequestContext(request))
