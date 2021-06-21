from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password, make_password
from user.models import User
from django.shortcuts import redirect, render


def sign_in(request):
    if request.method == "GET":
        return render(request, 'page/user/signin.html')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
        else:
            messages.error(request, '입력값을 확인해 주세요.')
        return redirect('sign_in')


def sign_up(request):
    if request.method == "GET":
        return render(request, 'page/user/signup.html')

    if request.method == "POST":
        username= request.POST['username']
        password=request.POST['password']
        user = User(
            username=username,
            password=make_password(password)
        )
        user.save()
        return redirect('sign_up')