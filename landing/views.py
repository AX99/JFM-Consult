from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import FormView, TemplateView
from .forms import ContactForm

class IndexView(TemplateView):
    template_name = 'index.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class  CoachingView(TemplateView):
    template_name = 'coaching.html'
    

# class BlogView(TemplateView):
#     template_name = 'blog.html'

# Latest comment below
# def contact(request):
#     form = ContactForm()
    
#     # if request.method == 'POST':
#     if request.is_ajax():
#         form = ContactForm(request.POST)

#         # first_name = request.POST['first_name']
#         # last_name = request.POST['last_name']
#         # email = request.POST['email']
#         # phone = request.POST['phone']
#         # message = request.POST['message']

#         if form.is_valid():
#             print("Post form is valid")
#             success = messages.success(request, 'Form submission successful') 
#             context = {'form': form, 'success': 'success'}
#             # return HttpResponse(success)
#             # return render(request, 'contact.html', context)
#             return JsonResponse({
#                 'msg': 'Success'
#             })
#         else:
#             print('Post form is INVALID')
#             success = messages.error(request, 'Form submission unsuccesful, try again')
#             context = {'form': form, 'success':success}
#             # return HttpResponse(success)
#             # return render(request, 'contact.html', context)
#             return JsonResponse({
#                 'msg': 'Error'
#             })
#     else:
#         context = {'form': form}
#         return render(request, 'contact.html', context)


# class ContactFormView(SuccessMessageMixin, FormView):
#     template_name = 'contact.html'
#     form_class = ContactForm
#     name = 'contact'
#     success_message = 'Your Message has been sent, you should receive a reply shortly. Thanks!'

#     def get(self,request, *args, **kwargs):
#         form = self.form_class()
#         return render(request, self.template_name, {'form' : form})

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             messages.success(request, 'Form submission successful')

#         return render(request, self.template_name, {'form': form})

#     def form_valid(self,form):
#         message = "{name} / {email} said: ".format(
#         first_name=form.cleaned_data.get('first_name'),
#         last_name=form.cleaned_data.get('last_name'),
#         email=form.cleaned_data.get('email'))
#         message += "\n\n{0}".format(form.cleaned_data.get('message'))
#         send_mail(
#             subject=form.cleaned_data.get('subject').strip(),
#             message=message,
#             from_email='contact-form@myapp.com',
#             recipient_list=[settings.LIST_OF_EMAIL_RECIPIENTS],
#         )
#         return super(ContactFormView, self).form_valid(form)  


def contact(request):
    form = ContactForm()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)

        # first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
        # email = request.POST['email']
        # phone = request.POST['phone']
        # message = request.POST['message']

        if form.is_valid():
            print("Post form is valid")
            success = messages.success(request, 'Form submission successful') 
            context = {'form': form, 'success': 'success'}
            # return HttpResponse(success)
            return render(request, 'contact.html', context)
        else:
            print('Post form is INVALID')
            success = messages.error(request, 'Form submission unsuccesful, try again')
            context = {'form': form, 'success':success}
            # return HttpResponse(success)
            return render(request, 'contact.html', context)
    else:
        context = {'form': form}
        return render(request, 'contact.html', context)
