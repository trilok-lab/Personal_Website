from django.db import models

# Create your models here.
class Customer(models.Model):
    gender_options = [
        ('F','Female'),
        ('M','Male'),
        ('O','Others')
    ]
    first_name = models.CharField(max_length=10)
    middle_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    mobile_number = models.CharField(max_length=15, unique= True)
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length = 1, choices=gender_options)

    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}|{self.mobile_number}| {self.age} |{self.gender}|"
    
class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_description = models.CharField(max_length=150)
    product_id = models.CharField(unique= True)

    cost_price = models.IntegerField()
    marked_price = models.IntegerField()
    selling_price = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return f"{self.product_name} {self.product_description} {self.selling_price}|"
