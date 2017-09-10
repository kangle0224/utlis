from django.shortcuts import render, redirect
from django.http import HttpResponse
from models import User, Asset
# Create your views here.

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        u = request.POST.get('user', None)
        p = request.POST.get('pwd', None)
        u_res = User.objects.filter(name=u)
        p_res = User.objects.filter(passwd=p)
        if len(u_res) != 0 and len(p_res) != 0:
            a_list = Asset.objects.filter(owner=u)
            a_list = Asset.objects.all()
            print a_list
            return render(request, 'asset.html', {'a_list': a_list})
        else:
            return render(request, 'login.html')
    else:
        return redirect("/index")

def get_db(request):
    a = User.objects.filter(name='kanasdfgle')
    print a

    return HttpResponse("db is ok!")
