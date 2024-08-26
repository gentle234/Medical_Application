from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Create and return a regular user with an email and password.
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and return a superuser with an email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
    )
    email = models.EmailField(unique=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    username = None  # Remove the username field

    USERNAME_FIELD = 'email'  # Use email as the unique identifier
    REQUIRED_FIELDS = []  # No additional required fields besides email and password

    objects = CustomUserManager()  # Assign the custom manager

    def __str__(self):
        return f"{self.email} ({self.get_user_type_display()})"