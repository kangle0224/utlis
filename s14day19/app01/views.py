from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse

# Create your views here.

# def login(request):
#     if request.method == "GET":
#         return render(request, "login.html")
#     elif request.method == "POST":
#         u = request.POST.get("user", None)
#         p = request.POST.get("pwd", None)
#         if u == "alex" and p == "123":
#             return render(request, "index.html")
#         else:
#             return render(request, "login.html")
#     else:
#         return redirect("/index")


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        # radio
        # gender = request.POST.get("gender", None)
        # print gender
        # checkbox
        # favor = request.POST.getlist("favor", None)
        # print favor
        # select
        # city = request.POST.getlist("city", None)
        # print city
        ff = request.FILES.get('file')
        import os
        f_path = os.path.join("upload", ff.name)
        f = open(f_path, "wb")
        for i in ff.chunks():
            f.write(i)
        f.close()
        return render(request, "login.html")
    else:
        return redirect("/index")



class Home(View):

    def dispatch(self, request, *args, **kwargs):
        print 'before'
        res = super(Home,self).dispatch(request, *args, **kwargs)
        print 'after'
        return res
    def get(self,request):
        print request.method
        return render(request, 'home.html')

    def post(self,request):
        print request.method
        return render(request, 'home.html')


user_dict = {
    '1':{'username': 'root1','email': 'root@qq.com'},
    '2':{'username': 'root2','email': 'root@qq.com'},
    '3':{'username': 'root3','email': 'root@qq.com'},
    '4':{'username': 'root4','email': 'root@qq.com'},
    '5':{'username': 'root5','email': 'root@qq.com'},
}



def index(request, **kwargs):
    print request.path_info, kwargs
    v = reverse('index', kwargs={"nid": 6})
    print v

    return render(request, "index.html", {'user_dict': user_dict})


def detail(request, nid):
    detail_info = user_dict[nid]
    print detail_info
    return render(request, 'detail.html', {'detail_info': detail_info})

