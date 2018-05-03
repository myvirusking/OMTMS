from django.shortcuts import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import *
from .models import *
from .forms import *
from django.db.models import Q
from django.template.context_processors import request
import re

# Create your views here.
def LoginUser(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        user_type=[i.myuser.username for i in MyUser.objects.all()]
        if user:
            if user.username in user_type:
                auth.login(request, user)
                return HttpResponseRedirect("/user/dashboard/")
            else:
                messages.error(request, '✘ You are Admin User Please Login via ', extra_tags='safe')
                return HttpResponseRedirect('/user/login/')
        else:
            messages.error(request, '✘ Incorrect Username and Password!')
            return HttpResponseRedirect('/user/login/')
    else:
        form = AuthenticationForm()
        return render(request, 'user/login.html', {'form': form})
    
    
def Dashboard(request):
    return render(request,"user/dashboard.html")

def LogoutUser(request):
    auth.logout(request)
    return HttpResponseRedirect('/user/login/')

def Registration(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            myusr=User.objects.get(username=request.POST['username'])
            MyUser.objects.create(myuser=myusr)
            #messages.success(request, 'You Account Registered Successfully!')
            return HttpResponseRedirect('/user/login/')
    else:
        form=RegistrationForm()
    return render(request, 'user/registration.html', {'form': form})


def Homepage(request):
    return render(request, 'user/homepage.html') 


def Movietheater(request):
    if request.method=="POST":
        value=request.POST['placen']
        obj=MovieTheater.objects.filter(Q(theaterplace__icontains=value[0:3]))
        print(obj)
        if obj:
            return render(request, 'user/movietheater.html',{'obj':obj})
        else: 
            return render(request, 'user/movietheater.html')
    else:
        return render(request, 'user/movietheater.html') 


def Moviename(request,pk):
    print(pk)
    pass


