from django.db import models
from event.models import Event
class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    ticket_type = models.CharField(max_length=50, choices=[('Regular', 'Regular'), ('VIP', 'VIP')])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.ticket_type} - {self.event.name}"