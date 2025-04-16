
from django.urls import path

from customer.views import retrieve_customer, save_customer , patch_customer

urlpatterns=[
    path('save/' , save_customer , name='Save Customer'),
    path('retrieve/' , retrieve_customer , name='Retrieve Customer'), # to get all Customer in list
    path('retrieve/<int:pk>/' , retrieve_customer , name='Retrieve Customer'), # to get 1 Customer
    path('update/<int:pk>/' , patch_customer , name='Update Customer'),
]