from django.shortcuts import render
import os
# Create your views here.
def home(request):
    if request.method == 'POST':
        g = request.POST.get('gender')
        f = request.POST.getlist('flavor')
        print f, g
        fbb = request.FILES.get('faaa')
        print fbb, type(fbb), fbb.name
        f_path = os.path.join('upload', fbb.name)
        with open(f_path, "wb") as a:
            for i in fbb.chunks():
                a.write(i)
    return render(request, 'home.html')