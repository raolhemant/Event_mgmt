from django.contrib import admin
from feedback.models import Feedback
# Register your models here.
@admin.register(Feedback)
class Admin_feedback(admin.ModelAdmin):
    list_display = ['event_id','user_id','rating']