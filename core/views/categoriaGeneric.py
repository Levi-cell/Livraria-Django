from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from core.serializers import CategoriaSerializer
from core.models import Categoria

"""
A classe importada RetrieveUpdateDestroyAPIView 
implementa para nós os métodos
GET, PUT, PATCH e DELETE.
"""


class CategoriasListGeneric(ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class CategoriaDetailGeneric(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

