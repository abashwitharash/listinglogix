from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# USER PROFILE
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    agency = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# PROPERTY
class Property(models.Model):
    address = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=50)
    details = models.TextField(blank=True, null=True)
    listed_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.address
