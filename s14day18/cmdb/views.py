# coding:utf-8
from django.shortcuts import render, redirect


# Create your views here.

def login(request):
    error_msg = ""
    if request.method == "POST":
        user = request.POST.get("username", None)
        pwd = request.POST.get("pwd", None)
        if user == "root" and pwd == '123':
            return redirect("/home")
        else:
            error_msg = "用户名或密码不正确"
    return render(request, 'login.html', {"error_msg": error_msg})

user_list = []

for i in range(3):
    user_list.append({"username": "alex"+str(i), "gender": "男", "email": "aaa@126.com"})


def home(request):
    if request.method == "POST":
        u = request.POST.get("user", None)
        e = request.POST.get("email", None)
        g = request.POST.get("gender", None)
        tem = {"username": u, "gender": g, "email": e}
        user_list.append(tem)
    return render(request, "home.html", {"user_list": user_list})