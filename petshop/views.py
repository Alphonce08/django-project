from django.shortcuts import render


def blogpage(request):
    return render(request, 'blog.html')

def indexpage(request):
    return render(request, 'index.html')

def homepage(request):
    return render(request, 'home.html')

def contactpage(request):
    return render(request, 'contact.html')

def servicespage(request):
    return render(request, 'services.html')
