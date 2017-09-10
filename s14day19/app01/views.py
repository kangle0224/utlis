from django.http import HttpResponse
from django.shortcuts import render, redirect


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

def index(request):
    return render(request, "index.html")
