from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)

    def __str__(self):
        return f"Dr. {self.name} - {self.specialty}"



# Create your models here.
