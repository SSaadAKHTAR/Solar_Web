from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def services(request):
    return render(request, 'services.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def projects(request):
    return render(request, 'projects.html')

def blog(request):
    return render(request, 'blog.html')

def calculator(request):
    return render(request, 'calculator.html')
