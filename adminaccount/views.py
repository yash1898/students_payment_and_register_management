from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login

def login_view(request):
    error=""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request,user)
                error="no"
            else:
                error="yes"
        except:
                error="yes"
    d={'error':error}
    return render(request,'adminaccount/login.html',d)

def logout_view(request):
    if not request.user.is_authenticated:
        return redirect('adminaccount:login')
    logout(request)
    return redirect('adminaccount:login')