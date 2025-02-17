from django.shortcuts import render
from rest_framework import generics

from .models import Women
from .serializers import WomenSerializer


# вью для таблицы women
class WomenAPIView(generics.ListAPIView):
    # передаём все строки таблицы women
    queryset = Women.objects.all()
    # сериализатор
    serializer_class = WomenSerializer