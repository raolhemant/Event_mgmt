from django.urls import path
from venue.views import Venue_ListView,Venue_updateView,Venue_DetailView,Venue_DeleteView,Venue_CreateView

urlpatterns =[
    path('Venue/',Venue_ListView.as_view(), name = 'venue_list'),
    path('Venue/<int:pk>/update',Venue_updateView.as_view(), name = 'venue_update'),
    path('Venue/<int:pk>/detail',Venue_DetailView.as_view() , name ='venue_detail' ),
    path('Venue/<int:pk>/delete',Venue_DeleteView.as_view(), name = 'venue_delete'),
    path('Venue/new/',Venue_CreateView.as_view(), name= 'venue_create')
]