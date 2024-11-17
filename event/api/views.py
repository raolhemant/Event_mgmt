# views.py
from rest_framework import generics
from event.models import Event
from event.api.serializers import Event_serializers

class Event_ListCreateAPIView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = Event_serializers

class Event_DetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = Event_serializers
