from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
def register(request):
    if(request.method=="post"):
        fn= request.post['first_name']
        ln=request.post['last_name']
        un=request.post['username']
        em=request.post['email']
        pas=request.post['password1']
        pas1=request.post['password2']
        if(pas==pas1):
            if(User.objects.filter(username=un).exists()):
                messages.info(request,'Username Taken!!')
            else:
                u=User.objects.create_user(username=un,password=pas,email=em)
                u.save()
                messages.success
        return redirect('/')
        #return render(request,"register.html")
