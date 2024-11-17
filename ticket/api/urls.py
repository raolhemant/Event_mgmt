from django.urls import path
from ticket.api.views import Ticket_listCreateAPIViews,Ticket_detailAPIViews

urlpatterns = [
    path('api/ticket/',Ticket_listCreateAPIViews.as_view(),name='list-create'),
    path('api/ticket/<int:pk>/',Ticket_detailAPIViews.as_view(),name='detail'),
]