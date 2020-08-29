from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm,UserUpadateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required


def Registration(request): 
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            messages.success(request,f"{username},you have created an account . Please log in here!")
            form.save()
            return redirect('login')
    else:               
        form = UserRegisterForm() 

    return render(request,'userinterface/registration.html',{"form":form})


@login_required
def Profile(request):
    if request.method == "POST":
        u_form = UserUpadateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                request.FILES,
                instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f"{request.user.username},your account has been updated!")  
            return redirect("profile") 
    else:
        u_form = UserUpadateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)             

    context = { 
        "u_form":u_form,
        "p_form":p_form,

    }

    return render(request,'userinterface/profile.html',context)
