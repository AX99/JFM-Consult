from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context= {}
    return render(request, 'index.html', context=context)

def about(request):
    context={}
    return render(request, 'about.html', context=context)

def coaching(request):
    context = {}
    return render(request,'coaching.html',context=context)
    
def blog(request):
    context = {}
    return render(request,'blog.html',context=context)

def contact(request):
    context = {}
    return render(request,'contact.html',context=context)