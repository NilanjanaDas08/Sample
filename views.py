from django.shortcuts import render,redirect,HttpResponse
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required #If it is authenticated then it will go to homepage
# Create your views here.
@login_required(login_url='Login')                          #If it is not authenticated it will stay in the samepage
def HomePage(request):
    return render(request,'Home.html')

def RegisterPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        pass2=request.POST.get('confirm_password')
        if pass1!=pass2:
         return HttpResponse("Your password is not correct")
        # Check if the username already exists
        if User.objects.filter(username=uname).exists():
            # Handle the error, e.g., by setting an error message
            return render(request, 'Register.html', {'error': 'Username already exists.'})
        try:
            # Create a new user
         User.objects.create_user(username=uname, email=email, password=pass1)
         return redirect('Login')
    
        except IntegrityError:
            return render(request, 'Register.html', {'error': 'Failed to create user.'})
        finally:
         pass
    else:
        return render(request, 'Register.html')
    return render(request,'Register.html')

def LoginPage(request):
    if request.method=='POST':
       username=request.POST.get('username')
       pass1=request.POST.get('pass')
       user=authenticate(request,username=username,password=pass1)
       if user is not None:
          login(request,user)
          return redirect('Home')
       else:
          return HttpResponse("Username or Password is incorrect")
    return render(request,'Login.html')
def LogoutPage(request):
   logout(request)
   return redirect('Login')
   
   
