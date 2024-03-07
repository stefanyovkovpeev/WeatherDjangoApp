from django.db import models
from django.contrib.postgres.fields import JSONField
from django.utils import timezone

class RandomCityData(models.Model):
    data = models.JSONField()
    date = models.DateTimeField(default=timezone.now)