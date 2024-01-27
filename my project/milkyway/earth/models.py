from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.IntegerField(max_length=10)
    email = models.EmailField(max_length=254)