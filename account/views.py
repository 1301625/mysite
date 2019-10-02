from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate , login ,logout as auth_logout

from account.forms import AccountCreateForm, AccountChangeForm ,LoginForm
from django.contrib.auth import login

def sign_in(request):
    """
    :param request:
    :return:
    """
    if request.method == "POST":
        form = LoginForm(request.POST )
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email ,password= password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('/')
    else:
        form = LoginForm

    return render(request,'registration/login.html', {'form': form})


def sign_up(request):
    if request.method == "POST":
        form = AccountCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else :
        form = AccountCreateForm

    return render(request, 'registration/signup.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('/')

