from rest_framework import views
from registration.models import Registration
from rest_framework import generics
from registration.api.serializers import Registration_serializers


class Registration_listCreateAPIView(generics.ListCreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = Registration_serializers

class Registration_DetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Registration.objects.all()
    serializer_class = Registration_serializers 