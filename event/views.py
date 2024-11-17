from django.shortcuts import render
# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Event
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.http import HttpResponse
from django.views import View
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from .models import Event 



class EventListView(LoginRequiredMixin,ListView,View):
    model = Event
    template_name = 'event_list.html'
    login_url = 'login'
    redirect_field_name = 'next' 
    

class EventPDFView(LoginRequiredMixin, View):
    login_url = 'login'
    redirect_field_name = 'next'
    
    def get(self, request, event_id, *args, **kwargs):
        # Create the HttpResponse object with the appropriate PDF headers
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="event_{event_id}.pdf"'

        # Create the PDF object using ReportLab
        pdf = canvas.Canvas(response, pagesize=letter)

        # Set up the title for the PDF
        pdf.setFont("Helvetica", 16)
        pdf.drawString(100, 750, f"Event Details for Event ID: {event_id}")

        # Get the event data using the provided event_id
        event = Event.objects.get(id=event_id)

        # Set font for the event details
        pdf.setFont("Helvetica", 12)

        # Write event details into the PDF
        y = 700  # Initial y position for content
        pdf.drawString(30, y, f"Event Name: {event.name}")
        y -= 20
        pdf.drawString(30, y, f"Description: {event.description}")
        y -= 20
        pdf.drawString(30, y, f"Event Start_time: {event.start_time}")
        y -= 20
        pdf.drawString(30, y, f"Event End_time: {event.end_time}")
        y -= 20
        pdf.drawString(30, y, f"Event venue: {event.venue}")
        y -= 20
        pdf.drawString(30, y, f"Event capacity: {event.capacity}")
        y -= 20
        pdf.drawString(30, y, f"Event Location: {event.location}")
        y -= 20
        

        # Finish the PDF
        pdf.showPage()
        pdf.save()

        # Return the PDF as a response
        return response


class EventDetailView(LoginRequiredMixin,DetailView):
    model = Event
    template_name = 'event_detail.html'
    login_url = 'login'
    redirect_field_name = 'next'

class EventCreateView(LoginRequiredMixin,CreateView):
    model = Event
    template_name = 'event_form.html'
    fields = ['name', 'description', 'capacity','venue','location']
    success_url = reverse_lazy('event_list')
    login_url = 'login'
    redirect_field_name = 'next'

class EventUpdateView(LoginRequiredMixin,UpdateView):
    model = Event
    template_name = 'event_form.html'
    fields = ['name', 'description', 'capacity','venue','location',]
    success_url = reverse_lazy('event_list')
    login_url = 'login'
    redirect_field_name = 'next'

class EventDeleteView(LoginRequiredMixin,DeleteView):
    model = Event
    template_name = 'event_confirm_delete.html'
    success_url = reverse_lazy('event_list')
    login_url = 'login'
    redirect_field_name = 'next'
