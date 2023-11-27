from django.db import models

# Create your models here.
class Student(models.Model):

    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    


class Address(models.Model):

    landmark = models.CharField(max_length=200)
    pincode = models.IntegerField()