from django.db import models

RATING = (
    (1, '⭐️'),
    (2, '⭐️⭐️'),
    (3, '⭐️⭐️⭐️'),
    (4, '⭐️⭐️⭐️⭐️'),
    (5, '⭐️⭐️⭐️⭐️⭐️'),
)

# Create your models here.
class Out(models.Model):
    title = models.CharField(max_length=255)
    restaurant_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    value = models.IntegerField(choices = RATING)
    taste = models.IntegerField(choices = RATING)
    atmosphere = models.IntegerField(choices = RATING)
    service = models.IntegerField(choices = RATING)
    date = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to='media')
    recommend = models.BooleanField()

    def __str__(self):
        return self.restaurant_name

class OutImage(models.Model):
    out = models.ForeignKey(Out, related_name='more_images', default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.image.url

class In(models.Model):
    title = models.CharField(max_length=255)
    dish_name = models.CharField(max_length=50)
    date = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.dish_name