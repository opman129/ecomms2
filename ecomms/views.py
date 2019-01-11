from django.shortcuts import render

def home(request):
    template_name = 'index.html'
    return render (request, template_name, {})

def elements(request):
    template_name = 'elements.html'
    return render (request, template_name, {})

def generic(request):
    template_name = 'generic.html'
    return render (request, template_name, {}) 