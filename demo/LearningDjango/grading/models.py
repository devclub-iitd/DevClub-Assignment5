from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Grade(models.Model):
    course = models.fields.CharField(max_length=6)
    marks = models.fields.IntegerField()
    student = models.ForeignKey(User, on_delete=models.CASCADE)
