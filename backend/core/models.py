from django.conf import settings
from django.db import models
class Data(models.Model):
    'Generated Model'
    name = models.CharField(max_length=256,)
    day = models.DateField()
    time = models.TimeField(null=True,blank=True,)

# Create your models here.
