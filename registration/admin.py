from django.contrib import admin
from .models import Registration
# Register your models here.
@admin.register(Registration)
class registrationadmin(admin.ModelAdmin):
    list_display = ['user_id','event_id']