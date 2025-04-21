from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def signup_page(request):
    return render(request,"signup.html")

def login_page(request):
    return HttpResponse("This is login page")

def logout_page(request):
    return HttpResponse("This is logout page")