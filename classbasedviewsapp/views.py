from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'home.html')
class GetInput(View):
    def get(self,request):
        return render(request,'getinput.html')
class PostInput(View):
    def get(self,request):
        return render(request,'postinput.html')
class Add(View):
    def get(self,request):
        p=int(request.GET["t1"])
        q=int(request.GET["t2"])
        r=p+q
        return HttpResponse("The Sum Of Two Values Is::"+str(r))
    def post(self,request):
        x=int(request.POST["t1"])
        y=int(request.POST["t2"])
        z=x+y
        return HttpResponse("The Sum Of Two Values Is::"+str(z))


