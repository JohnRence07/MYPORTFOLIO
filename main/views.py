from django.shortcuts import render

def home(request):
    return render(request, "main/index.html")

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')