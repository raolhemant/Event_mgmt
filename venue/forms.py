from django import forms
from venue.models import Venue

class venue_form(forms.ModelForm):
    class Meta:
        model = Venue
        fields = '__all__'