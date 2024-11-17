from django.contrib import admin
from venue.models import Venue
# Register your models here.
@admin.register(Venue)
class venueadmin(admin.ModelAdmin):
    list_display = ["name"]
     