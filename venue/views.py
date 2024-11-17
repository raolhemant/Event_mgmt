from django.shortcuts import render
from django.views.generic import ListView,UpdateView,DetailView,DeleteView,CreateView
from venue.models import Venue
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.
class Venue_ListView(LoginRequiredMixin,ListView):
    model = Venue
    template_name = 'venue_list.html'
    login_url = 'login'
    redirect_field_name = 'nxt'
    context_object_name = 'venues'

class Venue_CreateView(LoginRequiredMixin,CreateView):
    model = Venue
    fields ='__all__'
    template_name = 'venue_create.html'
    login_url  = 'login'
    redirect_field_name ='nxt'
    success_url = reverse_lazy('venue_list')

class Venue_updateView(LoginRequiredMixin,UpdateView):
    model = Venue
    fields = '__all__'
    template_name = 'venue_update.html'
    success_url = reverse_lazy('venue_list')
    login_url = 'login'
    redirect_field_name = 'nxt'

class Venue_DetailView(LoginRequiredMixin,DetailView):
    model = Venue
    template_name = 'venue_detail.html'
    login_url = 'login'
    redirect_field_name = 'nxt'

class Venue_DeleteView(LoginRequiredMixin,DeleteView):
    model = Venue
    template_name = 'venue_Delete.html'
    login_url = 'login'
    success_url = reverse_lazy('venue_list')
    redirect_field_name = 'nxt'