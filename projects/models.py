from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    technologies = models.CharField(max_length=255)
    github = models.CharField(max_length=50)
    netlify = models.CharField(max_length=50, default="")
    image = models.CharField(max_length=255)
    alt = models.CharField(max_length=100)
    display = models.CharField(max_length=10, blank=True, null=False, default="")

    def __str__(self):
        return self.name
