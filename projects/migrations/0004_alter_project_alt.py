# Generated by Django 3.2.3 on 2021-05-23 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20210523_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='alt',
            field=models.CharField(max_length=100),
        ),
    ]
