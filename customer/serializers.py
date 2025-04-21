from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Customer, Product

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class ProductSerial(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        #fields = ['product_name','product_id','product_description','selling_price']