from django.shortcuts import render,redirect
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout

#register user
def register_user(request):
    
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form=UserCreationForm()
    return render(request,'register.html',{'form':form})

#login user
def login_user(request):
    
    if request.method=="POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request,form.get_user())
            return redirect('/blog')
    else:
        form=AuthenticationForm()
    return render(request,'login.html',{'form':form})

#logout user
def logout_user(request):
    if request.method=="POST":
        logout(request)
        return redirect("/")