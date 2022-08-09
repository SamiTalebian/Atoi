from operator import mod
from django.db import models

class AtoiLog(models.Model):
    transaction_date = models.DateTimeField(auto_now_add=True)
    atoi_string = models.CharField(max_length=200)
    atoi_number = models.IntegerField()