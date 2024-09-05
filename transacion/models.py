from django.db import models

class Transaction(models.Model):
    title = models.CharField(max_length=25)
    date = models.DateField()
    amount = models.FloatField()


