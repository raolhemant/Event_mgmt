from django.urls import path
from venue.api.views import Venue_listCreateAPIView,Venue_DetailsAPIView


urlpatterns = [
    path('venue',Venue_listCreateAPIView.as_view(), name = 'list-Create'),
    path('venue/<int:pk>',Venue_DetailsAPIView.as_view(), name = 'Details')
]