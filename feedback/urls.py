from django.urls import path
from feedback.views import Feedback_CreateView,Feedback_ListView,Feedback_DetailView,Feedback_DeleteView,Feedback_UpdateView

urlpatterns = [
    path('', Feedback_ListView.as_view(), name='feedback_list'),
    path('feedback/create/', Feedback_CreateView.as_view(), name='feedback_create'),
    path('feedback/<int:pk>/', Feedback_DetailView.as_view(), name='feedback_detail'),
    path('feedback/<int:pk>/update/', Feedback_UpdateView.as_view(), name='feedback_update'),
    path('feedback/<int:pk>/delete/', Feedback_DeleteView.as_view(), name='feedback_delete'),
]


