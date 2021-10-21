from django.shortcuts import render
from rest_framework import generics
from .serializers import PostSerializer
from .models import Product


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = PostSerializer
