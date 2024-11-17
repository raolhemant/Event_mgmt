from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from registration.models import Registration
from registration.forms import RegistrationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q 
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from django.views import View
from reportlab.pdfgen import canvas



# ListView to list all registrations
class RegistrationListView(LoginRequiredMixin,ListView):
    model = Registration
    template_name = 'registration_list.html'  # Template to use
    context_object_name = 'registrations'      # Name for use in templates
    login_url = 'login'
    redirect_field_name = 'next'

    def get_queryset(self):
        queryset = super().get_queryset()
        # Retrieve filter parameters from the request's GET data
        query = self.request.GET.get('q', '')  # Example: search by keyword
        status_filter = self.request.GET.get('status', '')  # Example: filter by status

        # Apply filters based on the parameters
        if query:
            queryset = queryset.filter(
                Q(user__username__icontains=query) |  # Search in user's username
                Q(event__name__icontains=query) |     # Search in event name
                Q(email__icontains=query) # Example fields for searching
            )
        
        if status_filter:
            queryset = queryset.filter(status=status_filter)

        return queryset


# CreateView to handle new registration creation
class RegistrationCreateView(LoginRequiredMixin,CreateView):
    model = Registration
    form_class = RegistrationForm  # Form to use
    template_name = 'registration_form.html'  # Template for creating registrations
    success_url = reverse_lazy('registration_list')  # Redirect after successful creation
    login_url = 'login'
    redirect_field_name = 'next'


# UpdateView to handle editing an existing registration
class RegistrationUpdateView(LoginRequiredMixin,UpdateView):
    model = Registration
    form_class = RegistrationForm  # Same form for updating
    template_name = 'registration_form.html'  # Reuse the same template
    success_url = reverse_lazy('registration_list')  # Redirect after successful update
    login_url = 'login'
    redirect_field_name = 'next'


# DeleteView to handle deleting a registration
class RegistrationDeleteView(LoginRequiredMixin,DeleteView):
    model = Registration
    template_name = 'registration_confirm_delete.html'  # Confirmation template
    success_url = reverse_lazy('registration_list')  # Redirect after deletion
    login_url = 'login'
    redirect_field_name = 'next'


# DetailView to display registration details
class RegistrationDetailView(LoginRequiredMixin,DetailView):
    model = Registration
    template_name = 'registration_detail.html'  # Template to show registration details
    context_object_name = 'registration'        # Name for use in the template
    login_url = 'login'
    redirect_field_name = 'next'

class Registration_pdf(LoginRequiredMixin,View):
    login_url = 'login'
    redirect_field_name = 'next'
    def get(self, request, *args, **kwargs):
        # Create a PDF response
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="registrations.pdf"'

        # Create a PDF object using reportlab
        pdf = canvas.Canvas(response, pagesize=letter)

        # Set up the title for the PDF
        pdf.setFont("Helvetica", 16)
        pdf.drawString(100, 750, "Registration Data")

        # Get the registration data
        registrations = Registration.objects.all()

        # Set font for the table
        pdf.setFont("Helvetica", 12)

        # Initialize Y position for the content
        y = 700

        # Write table headers
        pdf.drawString(30, y, "User")
        pdf.drawString(150, y, "Event")
        pdf.drawString(270, y, "Ticket")
        pdf.drawString(390, y, "Email")
        pdf.drawString(510, y, "Status")
        y -= 20

        # Loop through registrations and write their data into the PDF
        for reg in registrations:
            if y < 50:  # Create a new page if we're running out of space
                pdf.showPage()
                y = 750

            pdf.drawString(30, y, f"{reg.user.username if reg.user else 'Unknown User'}")
            pdf.drawString(150, y, f"{reg.event.name if reg.event else 'Unknown Event'}")
            pdf.drawString(270, y, f"{reg.ticket.ticket_type if reg.ticket else 'No Ticket'}")
            pdf.drawString(390, y, reg.email)
            pdf.drawString(510, y, reg.get_status_display())  # Use the human-readable version of the status
            y -= 20

        # Finish the PDF
        pdf.showPage()
        pdf.save()

        # Return the response with the PDF
        return response




