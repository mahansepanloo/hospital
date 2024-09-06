from django.db import models
from accounts.models import Bimar

class Cat(models.Model):
    name = models.CharField(max_length=5000)

class Service(models.Model):
    category = models.ForeignKey(Cat, on_delete= models.CASCADE)
    type = models.CharField(max_length=250)
    bimar = models.ForeignKey('Bimar', on_delete= models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    price = models.IntegerField()

<<<<<<< HEAD
=======
    def __str__(self):
        return self.type
>>>>>>> ea39fdac1158f0adcf4b2659a2cf7484d10ee1e5


