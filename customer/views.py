from django.shortcuts import render
from rest_framework.decorators import api_view
#from django.urls import path
from django.http import request
from django.http import HttpResponse
# Create your views here
from django.urls import path, resolve
from rest_framework.reverse import reverse
from .models import Customer, Item
from rest_framework import generics, permissions
from .serializers import CustomerSerializer, ItemSerializer
from django.http import request

class CustomerCreate(generics.ListCreateAPIView):
    # API endpoint that allows creation of a new customer
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
"""class CustomerList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single customer by pk.
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer"""
    
        
class CustomerUpdate(generics.RetrieveUpdateDestroyAPIView):
    # API endpoint that allows a customer record to be updated.
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
"""class CustomerDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a customer record to be deleted.
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
"""
"""class ItemCreateView(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
"""