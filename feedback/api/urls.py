from django.urls import path
from feedback.api.views import Feedback_listCreateAPIView,Feedback_DetailAPIView

urlpatterns = [
    path('feedback/',Feedback_listCreateAPIView.as_view(),name='feedback-list-create'),
    path('feedback/<int:pk>/',Feedback_DetailAPIView.as_view(),name='feedback-detail')
]