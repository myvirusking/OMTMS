from django.shortcuts import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import *
from .models import *
from .forms import *
from django.db.models import Q
from django.template.context_processors import request
from django.contrib.auth.decorators import login_required

# Create your views here.
def LoginUser(request):
    if not request.user.is_authenticated:
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
    else:
        return HttpResponseRedirect('/user/dashboard/')
    
    
@login_required(login_url="/user/login/")
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
            messages.success(request, 'You Account Registered Successfully!')
            return HttpResponseRedirect('/user/login/')
    else:
        form=RegistrationForm()
    return render(request, 'user/registration.html', {'form': form})


def Homepage(request):
    return render(request, 'user/homepage.html') 


@login_required(login_url="/user/login/")
def Moveplace(request):
    if request.method=="POST":
        value=request.POST['placen']
        obj=MovieTheater.objects.filter(Q(theaterplace__icontains=value[0:3]))
        if obj:
            return render(request, 'user/movieplace.html',{'obj':obj})
        else: 
            return render(request, 'user/movieplace.html')
    else:
        return render(request, 'user/movieplace.html') 


@login_required(login_url="/user/login/")
def Moviename(request,pk,place):
    theater_obj=MovieTheater.objects.filter(id=pk)
    mylist=[]
    for i in theater_obj:
        theater_name=i.theatername
    
    obj=MovieName.objects.all()
    for i in obj:
        if i.theater.theatername == theater_name:
            image_name="images/{}.jpg".format(i.moviename)
            mylist.append((i.moviename,image_name,i.language))
    
    return render(request, 'user/moviename.html',{'mylist':mylist,"pk":pk,"place":place}) 


def Movieticket(request,pk,place,moviename,language):
    username="vinay"
    for i in MyUser.objects.all():
        if i.myuser.username==username:
            Tmyuser=i
    print(Tmyuser)
    theater=MovieTheater.objects.get(id=pk)
    for i in MovieName.objects.filter(moviename=moviename,language=language,theater=theater):
        Tmoviename=i
    print(Tmoviename)
    Tdate="2018-05-09"
    Ttime="19:34:42"

    return render(request, 'user/movieticket.html')
    









