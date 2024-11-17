# urls.py
from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from .views import Event_ListCreateAPIView, Event_DetailAPIView

urlpatterns = [
    # path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('api/events/', Event_ListCreateAPIView.as_view(), name='event-list-create'),
    path('api/events/<int:pk>/', Event_DetailAPIView.as_view(), name='event-detail'),
] 
