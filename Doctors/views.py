from rest_framework import generics
from rest_framework import filters
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorCreateView(generics.CreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'specialty']

class DoctorListView(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


# Create your views here.
