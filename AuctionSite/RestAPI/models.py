from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Vendor(models.Model):
    Vendor = models.OneToOneField(User, on_delete=models.CASCADE)
    CompanyName = models.CharField(max_length=50, blank=True, null=True)
    MobileNumber = models.CharField(max_length=12, blank=True, null=True)
    Telephone = models.CharField(max_length=12, blank=True, null=True)
    Address1 = models.CharField(max_length=128, blank=True, null=True)
    Address2 = models.CharField(max_length=128, blank=True, null=True)
    City = models.CharField(max_length=30, blank=True, null=True)
    PostalZip = models.CharField(max_length=10, blank=True, null=True)
    Country = models.CharField(max_length=30, blank=True, null=True)
    State = models.CharField(max_length=30, blank=True, null=True)
    def __str__(self):
        return self.Vendor.username

class Bidder(models.Model):
    Bidder = models.OneToOneField(User, on_delete=models.CASCADE)
    CompanyName = models.CharField(max_length=50, blank=True, null=True)
    MobileNumber = models.CharField(max_length=12, blank=True, null=True)
    Telephone = models.CharField(max_length=12, blank=True, null=True)
    Address1 = models.CharField(max_length=128, blank=True, null=True)
    Address2 = models.CharField(max_length=128, blank=True, null=True)
    City = models.CharField(max_length=30, blank=True, null=True)
    PostalZip = models.CharField(max_length=10, blank=True, null=True)
    Country = models.CharField(max_length=30, blank=True, null=True)
    State = models.CharField(max_length=30, blank=True, null=True)
    def __str__(self):
        return self.Bidder.username