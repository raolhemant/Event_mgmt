from rest_framework import serializers
from ticket.models import Ticket

class Ticket_serializers(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'