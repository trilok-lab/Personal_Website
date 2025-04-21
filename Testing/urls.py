from os import name
from django.urls import path
from .views import signup_page , login_page,logout_page

urlpatterns=[
    path('signup/',signup_page,name='signup_page'),
    path('login/',login_page,name='Login Page'),
    path('logout/',logout_page,name='Logout Page')
]