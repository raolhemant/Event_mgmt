from django.contrib import admin
from ticket.models import Ticket
# Register your models here.
@admin.register(Ticket)
class Ticketadmin(admin.ModelAdmin):
    list_display = ['event_id','price']