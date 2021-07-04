from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password, make_password
from user.models import User
from django.shortcuts import redirect, render


def sign_in(request):
    # 값을 읽고싶을때 GET - URL PARAMETER (http://awdaw.com?title=안녕하세요&param=메롱&param3=메롱2)
    # 값을 지우고싶을땐 DELETE

    # 값을 수정 PUT - body 
    # 값을 생성 POST
    if request.method == "GET":
        return render(request, 'page/signin.html')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('board')
        else:
            messages.error(request, '입력값을 확인해 주세요.')
            return redirect('sign_in')


def sign_up(request):
    if request.method == "GET":
        return render(request, 'page/signup.html')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        nickname = request.POST['nickname']
        
        # exists - 존재하면 True, 존재하지 않으면 False
        if User.objects.filter(username=username).exists():
            messages.error(request, '이미 존재하는 아이디입니다')
            return redirect('sign_up')
        else:
            user = User(
                username=username,
                password=make_password(password),
                nickname=nickname,
            )
            user.save()
            login(request, user)
            return redirect('board')


def sign_out(request):
    if request.method == "GET":
        logout(request)
        return redirect('board')