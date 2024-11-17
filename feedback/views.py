from django.shortcuts import render
from django.urls import reverse_lazy
from feedback.models import Feedback
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views.generic import (
    ListView,
    DeleteView,
    CreateView,
    UpdateView,
    DetailView,
)

# Create your views here.
class Feedback_ListView(LoginRequiredMixin,ListView):
    model = Feedback
    template_name = 'feedback_list.html'
    context_object_name = 'feedbacks'
    login_url = 'login'
    redirect_field_name = 'nxt'
    
    

class Feedback_CreateView(LoginRequiredMixin,CreateView):
    model = Feedback
    template_name = 'feedback_create.html'
    success_url = reverse_lazy('feedback_list')
    fields = '__all__'
    login_url = 'login'
    redirect_field_name = 'nxt'
    
    

class Feedback_DeleteView(LoginRequiredMixin,DeleteView):
    model = Feedback
    template_name = 'feedback_delete.html'
    success_url = reverse_lazy('feedback_list')
    login_url = 'login'
    redirect_field_name = 'nxt'

class Feedback_UpdateView(LoginRequiredMixin,UpdateView):
    model = Feedback
    template_name = 'feedback_edit.html'
    fields = '__all__'
    success_url = reverse_lazy('feedback_list')
    login_url = 'login'
    redirect_field_name = 'nxt'

class Feedback_DetailView(LoginRequiredMixin,DetailView):
    model = Feedback
    template_name = 'feedback_detail.html'
    login_url = 'login'
    redirect_field_name = 'nxt'