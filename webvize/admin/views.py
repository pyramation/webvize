from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from admin.forms import *
from django.core.mail import send_mail
from django.core.mail import EmailMessage

def terms(request):
    return render_to_response('legal/terms.html', {'sitename':'BenchRank'}, context_instance = RequestContext(request))

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']

            recipients = ['dan@benchrank.com']

            subject = "message from: %s" % sender;
#             email = EmailMessage("%s : from %s" % (subject, sender), message, to=recipients)
#             email.send()
            send_mail(subject, message, sender, recipients)
            return render_to_response('contact/thanks.html', context_instance = RequestContext(request))
    else:
        form = ContactForm()
    return render_to_response('contact/contact.html', {'form':form, 'action':'/contact/', 'submit':'Submit'}, context_instance = RequestContext(request))
