# Generated by Django 3.2.3 on 2021-05-24 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_alter_project_netlify'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='netlify',
            field=models.CharField(max_length=50),
        ),
    ]