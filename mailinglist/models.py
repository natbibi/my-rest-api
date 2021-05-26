from django.db import models
from django.dispatch import receiver
from django.template.loader import render_to_string 
from django.core.mail import send_mail
from django.db.models.signals import post_save

# Create your models here.
class Mailing(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.name


@receiver(post_save, sender= Mailing)
def new(sender, instance, created, **kwargs):
    
        context = {
            'user': instance.name,
        }

        send_mail(
            'Just a quick hello 👋🏼', 
            msg, 
            'natalie.wuwu@googlemail.com',
            [instance.email],
            fail_silently=False,
            html_message = render_to_string('index.html', context),
        )