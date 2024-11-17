from django.db import models
from event.models import Event
from ticket.models import Ticket
from django.contrib.auth.models import User
class Registration(models.Model):
    class RegistrationStatus(models.IntegerChoices):
        ONGOING = 1, "ONGOING"
        COMPLETE = 2, "COMPLETE"
        CANCELLED = 3, "CANCELLED"

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True)
    ticket = models.ForeignKey(Ticket, on_delete=models.SET_NULL, null=True)  # Link to the Ticket model
    email = models.EmailField()
    registration_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=RegistrationStatus.choices, default=RegistrationStatus.ONGOING)

    def __str__(self) -> str:
        return f'{self.user.username if self.user else "Unknown User"} - {self.event.name if self.event else "Unknown Event"} - {self.ticket.ticket_type if self.ticket else "No Ticket"}'