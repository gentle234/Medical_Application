from django.urls import path
from .views import AppointmentCreateView, AppointmentListView

urlpatterns = [
    path('appointments/', AppointmentListView.as_view(), name='appointment-list'),
    path('appointments/create/', AppointmentCreateView.as_view(), name='appointment-create'),
]
