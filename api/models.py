from django.db import models

# Create your models here.
class Programmer(models.Model):
    fullName = models.CharField(max_length=100)
    nickName = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default=True)

class React(models.Model):
    employee = models.CharField(max_length=30)
    department = models.CharField(max_length=200)