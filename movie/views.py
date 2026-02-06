from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {'name': 'Hellen'})

def about(request):
    return render(request, 'about.html')
