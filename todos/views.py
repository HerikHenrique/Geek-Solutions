from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
 return render(request, "todos/home.html")

def page1(request):
 return render(request, "todos/page1.html")