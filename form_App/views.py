from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='signin')
def homePage(request):

    return render(request, 'home.html')

def signUpPage(request):
    if request.method=="POST":
        user_name = request.POST.get("userName")
        email_id = request.POST.get("email")
        user_pwd = request.POST.get("password")
        user_cmpwd = request.POST.get("confirm_password")

        if user_pwd!=user_cmpwd:
            return HttpResponse("Your Password & Confirm Password are not same!")
        else:
            my_user =  User.objects.create_user(user_name, email_id, user_pwd)
            my_user.save()
            return redirect("signin")
    return render(request, 'registration.html')

def signInPage(request):

    if request.method=="POST":
        usrname = request.POST.get("username")
        passWord = request.POST.get("pass")

        user = authenticate(request, username=usrname, password=passWord) 
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect")
    return render(request, 'login.html')


def logOutPage(request):
    logout(request)
    return redirect("signin")