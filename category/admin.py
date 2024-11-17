from django.contrib import admin
from category.models import Category
# Register your models here.
@admin.register(Category)
class Admincategory(admin.ModelAdmin):
    list_display = ['name']