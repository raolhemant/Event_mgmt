from django import forms
from ticket.models import Ticket

class Registration_Form(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'