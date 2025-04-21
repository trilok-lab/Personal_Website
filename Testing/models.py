from django.db import models

# Create your models here.
class user (models.Model):
    first_name= models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    contact_no = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
