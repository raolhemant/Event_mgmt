from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,UpdateView,DeleteView,CreateView
from ticket.models import Ticket
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Ticket_ListView(LoginRequiredMixin,ListView):
    model = Ticket
    template_name = "ticket_list.html"
    login_url = 'login'
    redirect_field_name = 'nxt'
    context_object_name = 'tickets'


class Ticket_DetailView(LoginRequiredMixin,DetailView):
    model = Ticket
    template_name ="ticket_detail.html"
    context_object_name = 'ticket'
    login_url = 'login'
    redirect_field_name = 'nxt'

class Ticket_updateView(LoginRequiredMixin,UpdateView):
    model = Ticket
    fields = '__all__'
    template_name = 'ticket_update.html'
    success_url = reverse_lazy('ticket_list')
    login_url = 'login'
    redirect_field_name = 'nxt'

class Ticket_deleteView(LoginRequiredMixin,DeleteView):
    model = Ticket
    template_name = 'ticket_delete.html'
    success_url = reverse_lazy('ticket_list')  
    login_url = 'login'
    redirect_field_name = 'nxt'

class Ticket_createView(LoginRequiredMixin,CreateView):
    model = Ticket
    fields = '__all__'
    template_name = 'ticket_create.html'
    success_url = reverse_lazy('ticket_list')
    login_url = 'login'
    redirect_field_name ='nxt'