from django.db import models

# Create your models here.
class employees(models.Model): #employees is the table name
    employee_name=models.CharField(max_length=255)
    email=models.EmailField()
    section=models.CharField(max_length=255)
    salary=models.IntegerField()