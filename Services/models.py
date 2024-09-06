from django.db import models
from accounts.models import Bimar

class Cat(models.Model):
    name = models.CharField(max_length=5000)

class Service(models.Model):
    category = models.ForeignKey(Cat, on_delete= models.CASCADE)
    bimar = models.ForeignKey('Bimar', on_delete= models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    price = models.IntegerField()

    def __str__(self):
        return self.category.name



