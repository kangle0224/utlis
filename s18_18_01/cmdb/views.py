from django.shortcuts import render, HttpResponse

# Create your views here.
def c_login(request):
    return HttpResponse("<h5>Hello cmdb!<h5>")
