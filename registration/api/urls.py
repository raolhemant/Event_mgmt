from django.urls import path
from registration.api.views import Registration_listCreateAPIView , Registration_DetailAPIView

urlpatterns = [
    path('registration/', Registration_listCreateAPIView.as_view(), name = "registration-list-create"),
    path ('registration/<int:pk>/', Registration_DetailAPIView.as_view(), name = 'registration-details'),

]