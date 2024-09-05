from django.db import models

class Transaction(models.Model):
    title = models.CharField(max_length=25)
    date = models.DateTimeField(auto_now=True)
    amount = models.FloatField()


