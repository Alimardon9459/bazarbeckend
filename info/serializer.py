from rest_framework import serializers
from .models import *
from asyncore import read

class Products__Serializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

class Cartagory__Serializer(serializers.ModelSerializer):
    products = Products__Serializer(many=True, read_only=True)
    class Meta:
        model = Cartagory
        fields = ["id" , "name" , "img" , "info" , "products"]

class Orders__Serializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'

class Users__Serializer(serializers.ModelSerializer):
    orders = Orders__Serializer(many=True, read_only=True)
    class Meta:
        model = Users
        fields = ["id" , "fname" , "tel_number" , "location" , "comment" , "orders"]
