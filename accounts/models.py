from django.db import models
from django.contrib.auth.models import User

class Bimar(models.Model):
    user = models.CharField(max_length=5000)

    def __str__(self):
        return self.user



class Nurse(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    shift = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username