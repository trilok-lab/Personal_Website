
from os import name
from django.urls import path

from customer.views import get_product, retrieve_customer, save_customer , patch_customer, save_product

urlpatterns=[
    path('save/' , save_customer , name='Save Customer'),
    path('retrieve/' , retrieve_customer , name='Retrieve Customer'), # to get all Customer in list
    path('retrieve/<int:pk>/' , retrieve_customer , name='Retrieve Customer'), # to get 1 Customer
    path('update/<int:pk>/' , patch_customer , name='Update Customer'),

    path ('s_product/',save_product, name='Save Product Detail'),
    path('g_product/', get_product, name='Get Product Detail')
]