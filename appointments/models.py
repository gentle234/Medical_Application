from django.db import models
from django.conf import settings
from Doctors.models import Doctor

class Appointment(models.Model):
    STATUS_CHOICES = (
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )

    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='scheduled')

    def __str__(self):
        return f"Appointment with Dr. {self.doctor.name} for {self.patient.email} on {self.date} at {self.time}"


# Create your models here.
