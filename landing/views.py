from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import FormView, TemplateView
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError, EmailMessage


class IndexView(TemplateView):
    template_name = 'index.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class  CoachingView(TemplateView):
    template_name = 'coaching.html'
    

# class BlogView(TemplateView):
#     template_name = 'blog.html'

def contact(request):
    form = ContactForm()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            print("Post form is valid")
            subject = f'Message from {form.cleaned_data["first_name"]} {form.cleaned_data["last_name"]}'
            message = form.cleaned_data["message"]
            sender = ["info@jfmconsult.co.uk"]
            recipient = ["info@jfmconsult.co.uk"]
            headers = {'Reply-To': f'{form.cleaned_data["email"]}'}
            
            try:
                msg = EmailMessage(subject, message, sender, recipient, headers=headers)
                msg.send(fail_silently=True)
            except BadHeaderError:
                return HttpResponse("Invalid Header Found")
            success = messages.success(request, 'Form sent! You should receive an email confirmation shortly - (Check your spam)')
            return HttpResponseRedirect('/contact/', success)
        else:
            print('Post form is INVALID')
            success = messages.error(request, 'Form submission unsuccesful, try again')
            context = {'form': form, 'success':success}
            return render(request, 'contact.html', context)
    else:
        context = {'form': form}
        return render(request, 'contact.html', context)
