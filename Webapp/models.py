from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id=models.IntegerField(max_length=10)
    emp_fname=models.CharField(max_length=15)
    emp_lname=models.CharField(max_length=10)

class Salary(models.Model):
    salary=models.ForeignKey(Employee,on_delete=models.CASCADE())


