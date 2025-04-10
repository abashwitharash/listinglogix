from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# USER PROFILE
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True) 
    phone = models.CharField(max_length=100, blank=True, null=True)  
    agency = models.CharField(max_length=100, blank=True, null=True) 


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# PROPERTY
class Property(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('active_under_contract', 'Active Under Contract'),
        ('pending', 'Pending'),
        ('sold', 'Sold'),
        ('expired', 'Expired'),
        ('cancelled', 'Cancelled'),
    ]

    address = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='available')
    details = models.TextField(blank=True, null=True)
    listed_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    date_posted = models.DateField(default=date.today) 
    dom = models.IntegerField(blank=True, null=True)   
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.address
    
    def get_absolute_url(self):
        return reverse('list-detail', kwargs={'list_id': self.id})
