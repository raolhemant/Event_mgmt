from rest_framework import generics
from category.models import Category
from category.api.serializers import Category_serializers

class Category_ListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = Category_serializers

class Category_DetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = Category_serializers