from django import forms
from feedback.models import Feedback

class Feedback_forms(forms.ModelForm):
    class Meta:
        model =Feedback
        fields = "__all__" 
