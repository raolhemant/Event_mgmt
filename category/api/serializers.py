from rest_framework import serializers
from category.models import Category

class Category_serializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'