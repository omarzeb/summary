from django.db import models
from datetime import datetime
from simple_history.models import HistoricalRecords
# Create your models here.


class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    timestamp = models.DateTimeField(default = datetime.now())

    def __str__(self):
        return self.name



class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique= True)
    email = models.CharField(max_length=100)
    department = models.ForeignKey(Department, models.DO_NOTHING)
    timestamp = models.DateTimeField(default = datetime.now())
    history = HistoricalRecords()

    def __str__(self):
        return self.first_name

