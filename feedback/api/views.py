from rest_framework import views
from rest_framework import generics
from feedback.models import Feedback
from feedback.api.serializers import Feedback_serializers


class Feedback_listCreateAPIView(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = Feedback_serializers

class Feedback_DetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = Feedback_serializers
