from rest_framework import serializers
from venue.models import Venue

class venue_serializers(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = '__all__'