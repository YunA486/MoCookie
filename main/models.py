from django.db import models

class first(models.Model):
    name = models.CharField(max_length=10)
    url = models.URLField()

