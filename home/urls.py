from django.contrib import admin
from django.urls import path
from . import views

#Django admin header customization(learn from harry)
admin.site.site_header ="Login to Developer Hemant"
admin.site.site_title = "Welcome to hemant Dashboard"
admin.site.index_title = "Welcome to this Portal"

urlpatterns = [
    path ('register/', views.register_page, name = 'register'),
    path('login/', views.login_page, name= 'login'),
    path('logout/', views.logoutUser, name='logout'),
]