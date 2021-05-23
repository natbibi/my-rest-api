from django.db import models

# Create your models here.
class Destination(models.Model):
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    image = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.city