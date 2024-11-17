import filters
from registration.models import Registration
  

class registration_filter():
    class Meta:
        model = Registration
        fields = '__all__'