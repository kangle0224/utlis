# coding: utf-8
from django.shortcuts import render, HttpResponse, redirect


# Create your views here.
def login(request):
    error_msg = ""
    if request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        if user == 'root' and pwd == '123':
            return redirect('http://www.baidu.com')
        else:
            error_msg = "用户名或密码错误"

    return render(request, 'login.html', {'error_msg': error_msg})

test_list = [
    {'name': 'alex', 'gender': 'nan', 'age': 26},
    {'name': 'dalao', 'gender': 'nan', 'age': 26},
    {'name': 'eric', 'gender': 'nv', 'age': 26}
]
def home(request):
    if request.method == 'POST':
        u = request.POST.get('user')
        g = request.POST.get('gender')
        a = request.POST.get('age')
        temp = {'name': u, 'gender': g, 'age': a}
        test_list.append(temp)
    return render(request, 'home.html', {'test_list': test_list})