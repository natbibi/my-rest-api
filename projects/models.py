from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    technologies = models.CharField(max_length=255)
    github = models.CharField(max_length=50)
    netlify = models.CharField(max_length=50)
    image = models.CharField(max_length=255)
    alt = models.CharField(max_length=30)
    display = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.name
