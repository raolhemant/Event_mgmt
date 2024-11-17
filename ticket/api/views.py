from rest_framework import views
from rest_framework import generics
from ticket.models import Ticket
from ticket.api.serializers import Ticket_serializers



class Ticket_listCreateAPIViews(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = Ticket_serializers


class Ticket_detailAPIViews(generics.RetrieveDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = Ticket_serializers
    