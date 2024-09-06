from django.db import models
from accounts.models import Bimar


class Service(models.Model):
    type = models.CharField(max_length=250)
    bimar = models.ForeignKey('Bimar', on_delete= models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    price = models.IntegerField()

