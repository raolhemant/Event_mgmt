from django.urls import path
from ticket.views import Ticket_ListView,Ticket_DetailView,Ticket_updateView,Ticket_deleteView,Ticket_createView


urlpatterns = [
    path('tickets/', Ticket_ListView.as_view(), name='ticket_list'),
    path('tickets/new/',Ticket_createView.as_view(), name='ticket_create'),
    path('tickets/<int:pk>/', Ticket_DetailView.as_view(), name='ticket_detail'),
    path('tickets/<int:pk>/update/', Ticket_updateView.as_view(), name='ticket_update'),
    path('tickets/<int:pk>/delete/', Ticket_deleteView.as_view(), name='ticket_delete')
]