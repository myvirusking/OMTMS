from django.shortcuts import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import *


# Create your views here.

def LoginUser(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return HttpResponseRedirect("/login/")
        else:
            messages.error(request, '✘ Invaild Username and Password!')
            return HttpResponseRedirect('/user/login/')
    else:
        form = AuthenticationForm()
        return render(request, 'OMTMS/login.html', {'form': form})