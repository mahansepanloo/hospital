from django.db import models
from accounts.models import Bimar
from Services.models import Service

class Orders(models.Model):
    bimar = models.ForeignKey(Bimar, on_delete=models.CASCADE, related_name='orders')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='orders')
    price = models.BigIntegerField()
    date = models.DateTimeField(auto_now_add=True)



    class Meta:
        ordering = ['-date']