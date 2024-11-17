from django.db import models
from event.models import Event
from django.contrib.auth.models import User
# Create your models here.
class Feedback(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.SET_NULL,null=True)
    user_id = models.ForeignKey(User,on_delete=models.SET_NULL ,null=True)
    rating  = models.CharField(max_length=100)
    comment = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.rating