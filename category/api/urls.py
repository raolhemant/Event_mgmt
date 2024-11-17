from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from category.api.views import (
    Category_ListCreateAPIView,
    Category_DetailAPIView
)

urlpatterns = [
    path('category/', Category_ListCreateAPIView.as_view(), name='Ca-list-create'),
    path('category/<int:pk>/', Category_DetailAPIView.as_view(), name='Ca-detail'),
]