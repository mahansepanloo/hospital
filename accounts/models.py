from django.db import models
from django.contrib.auth.models import User
class Walet(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    wallet = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.user.username