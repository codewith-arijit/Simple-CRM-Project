from django.forms import forms
from django.shortcuts import render
from rest_framework.decorators import api_view
#from django.urls import path
from django.http import request
from django.http import HttpResponse
# Create your views here
from django.urls import path, resolve
from rest_framework.reverse import reverse

from customer.forms import CustomerForm
from .models import Customer, Item
from rest_framework import generics, permissions
from .serializers import CustomerSerializer, ItemSerializer
from django.http import request
from .forms import CustomerForm
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


def customer_template(request):
    text_submitted = Customer.objects.values('name', 'email')
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            #print(driver_text)
            
            return render(request, 'thanks.html', {'text_submitted':text_submitted})

    else:
        form = CustomerForm()
    return render(request, 'customer.html',{'form':form})