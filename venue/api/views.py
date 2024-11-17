from rest_framework import views
from venue.api.serializers import venue_serializers
from rest_framework import generics
from venue.models import Venue


class Venue_listCreateAPIView(generics.ListCreateAPIView):
    queryset = Venue.objects.all()
    serializer_class = venue_serializers

class Venue_DetailsAPIView(generics.RetrieveDestroyAPIView):
    queryset = Venue.objects.all()
    serializer_class = venue_serializers