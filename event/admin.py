from django.contrib import admin
from event.models import Event
# Register your models here.
@admin.register(Event)
class Admin_event (admin.ModelAdmin):
    list_display = ['name']
    