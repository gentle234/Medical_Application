from django.urls import path
from .views import DoctorCreateView, DoctorListView

urlpatterns = [
    path('Doctors/', DoctorListView.as_view(), name='doctor-list'),
    path('Doctors/search/', DoctorListView.as_view(), name='doctor-search'),
    path('Doctors/create/', DoctorCreateView.as_view(), name='doctor-create'),
    
]
