from django.shortcuts import render

# Create your views here.
def home(request):
   
    return render(request,'home.html')
    
def static(request):
    return render(request, 'static.html')

def about(request):
    return render(request, 'about.html')

def login(request):
    return render(request, 'login.html')

def gallary(request):
    return render(request, 'gallary.html')

def contact(request):
    return render(request, 'contact.html')