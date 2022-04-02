from django.db import models
from django.db.models.fields import CharField,DateField,EmailField,PositiveIntegerField

# Create your models here.

class CompanyRegister(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.fname+" "+self.lname

class Customers(models.Model):
    company=models.ForeignKey('CompanyRegister',on_delete=models.CASCADE,blank=True, null=True)
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.fname+" "+self.lname