from django.urls import path
from . import views

urlpatterns = [
    path('registrations/', views.RegistrationListView.as_view(), name='registration_list'),
    path('registration/new/', views.RegistrationCreateView.as_view(), name='registration_create'),
    path('registration/<int:pk>/edit/', views.RegistrationUpdateView.as_view(), name='registration_edit'),
    path('registration/<int:pk>/delete/', views.RegistrationDeleteView.as_view(), name='registration_delete'),
    path('registration/<int:pk>/', views.RegistrationDetailView.as_view(), name='registration_detail'),
    path('registartion/pdf/', views.Registration_pdf.as_view(), name = 'reg_pdf'),
]



