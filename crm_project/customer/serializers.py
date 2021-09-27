from rest_framework import serializers
from .models import Customer
from .models import Item

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer 
        fields = ['pk', 'name', 'email', 'created']

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ['pk', 'name', 'price']
