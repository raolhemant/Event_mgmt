from django.db import models
from venue.models import Venue
# from 
# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    # username = models.ForeignKey(User ,)
    location = models.CharField(max_length=100)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE , null= True)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now=True)
    capacity = models.CharField(max_length=100)
    image = models.ImageField( null=True)


    def __str__(self) -> str:
        return self.name


