from .models import *
from .serializer import *
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class Cartagory__ViewSet(ModelViewSet):
    queryset = Cartagory.objects.all()
    serializer_class = Cartagory__Serializer

class Products__ViewSet(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = Products__Serializer

class Users__ViewSet(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = Users__Serializer

class Orders__ViewSet(ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = Orders__Serializer  


