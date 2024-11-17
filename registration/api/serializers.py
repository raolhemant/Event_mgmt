from rest_framework import serializers
from registration.models import Registration

class Registration_serializers (serializers.ModelSerializer):
    class Meta():
        model = Registration
        fields = '__all__'

