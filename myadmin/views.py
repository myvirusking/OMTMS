from django.shortcuts import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import *
from user.models import MyUser

# Create your views here.

def Myadminlogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        user_type=[i.myuser.username for i in MyUser.objects.all()]
        if user:
            if user.username not in user_type:
                auth.login(request, user)
                return HttpResponseRedirect("/myadmin/dashboard/")
            else:
                messages.error(request, '✘ You are Not Authorized Permission To AdminLogin. Please Login Via ', extra_tags='safe')
                return HttpResponseRedirect('/myadmin/login/')
        else:
            messages.error(request, '✘ Incorrect Username and Password!')
            return HttpResponseRedirect('/myadmin/login/')
    else:
        form = AuthenticationForm()
        return render(request, 'myadmin/login.html', {'form': form})

   
def Dashboard(request):
    return render(request,"myadmin/dashboard.html")

def LogoutAdmin(request):
    auth.logout(request)
    return HttpResponseRedirect('/myadmin/login/')