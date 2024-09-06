from django.db import models
from accounts.models import *
from Services.models import *
class Orders(models.Model):
    bimar = models.ForeignKey(Bimar,on_delete=models.CASCADE)
    price = models.BigIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    service = models.ForeignKey(Service,on_delete=models.CASCADE)