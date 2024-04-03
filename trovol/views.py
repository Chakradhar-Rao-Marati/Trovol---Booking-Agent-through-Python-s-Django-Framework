from django.shortcuts import render
from .models import Destination

def blog(request):
    return render(request,'blog.html')
def client(request):
    return render(request,'client.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def packages(request):
    d1=Destination.objects.all()
    return render(request,'packages.html',{'dest': d1})
def index(request):
    d1= Destination.objects.all()
    return render(request,'index.html',{'dest': d1})
