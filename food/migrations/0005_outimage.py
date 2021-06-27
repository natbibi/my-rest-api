# Generated by Django 3.2.4 on 2021-06-27 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_in_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='OutImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media')),
                ('out', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='food.out')),
            ],
        ),
    ]
