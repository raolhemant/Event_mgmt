from rest_framework import serializers
from feedback.models import Feedback

class Feedback_serializers(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

