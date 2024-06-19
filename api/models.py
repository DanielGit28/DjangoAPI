from django.db import models

# Create your models here.
class Programmer(models.Model):
    fullName = models.CharField(max_length=100)
    nickName = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField(max_length=2)
    is_active = models.BooleanField(default=True)