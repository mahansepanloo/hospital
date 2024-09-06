from django.db import models
from django.contrib.auth.models import User

class Bimar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=100)
    years_of_experience = models.IntegerField()

    def __str__(self):
        return self.user.username

class Nurse(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    shift = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username