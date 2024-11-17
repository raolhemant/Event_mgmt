from django.db import models
class Venue(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    capacity = models.IntegerField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name