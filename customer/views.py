from functools import partial
from itertools import product
from urllib import response
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

import customer

from .models import Customer, Product
from .serializers import CustomerSerializer, ProductSerial
from customer import serializers

# Create your views here.
# save customer info
@api_view(['POST'])
def save_customer(request):
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"Customer saved Successfully !!!", "data":serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#update customer info
@api_view(['PATCH'])
def patch_customer(request , pk):
    try : 
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return Response ({"error":"Customer does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = CustomerSerializer(customer, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response ({"message":"Details Updated Successfully !!!!","data":serializer.data}, status=status.HTTP_200_OK)
    return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
# retrieve customer info
@api_view(['GET'])
def retrieve_customer(request, pk=None ):# pk will only be used when asking for a perticular customer 
    if pk is not None:
        #Retrieve Single Customer
        customer = get_object_or_404(Customer,pk=pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        #Retrieve Customer List
        customer=Customer.objects.all()
        serializer = CustomerSerializer(customer, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

@api_view(['POST'])
def save_product(request):
    serial = ProductSerial(data=request.data)
    if serial.is_valid():
        serial.save()
        return Response({"message":"Product Detail saved successfully", "data":serial.data} , status=status.HTTP_201_CREATED)
    return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_product(request):
    product = Product.objects.all()
    serial = ProductSerial(product, many=True)
    return Response(serial.data, status=status.HTTP_200_OK)

