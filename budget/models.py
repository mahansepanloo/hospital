from django.db import models

class Plan(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()
    req_budget = models.FloatField()
    sat_budget = models.FloatField()
    status = models.CharField(max_length=10)


