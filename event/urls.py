from django.urls import path
from . import views  
from .views import (
    EventListView,
    EventDetailView,
    EventCreateView,
    EventUpdateView,
    EventDeleteView,
    EventPDFView

)

urlpatterns = [
    path('', views.EventListView.as_view(), name='event_list'),
    path('event/<int:pk>/', views.EventDetailView.as_view(), name='event_detail'),
    path('event/new/', views.EventCreateView.as_view(), name='event_create'),
    path('event/<int:pk>/edit/', views.EventUpdateView.as_view(), name='event_edit'),
    path('event/<int:pk>/delete/', views.EventDeleteView.as_view(), name='event_delete'),
    path('event/pdf/<int:event_id>/',views.EventPDFView.as_view(), name='event_pdf'),
]
