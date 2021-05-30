# Generated by Django 3.2.3 on 2021-05-30 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_in'),
    ]

    operations = [
        migrations.AddField(
            model_name='out',
            name='date',
            field=models.DateField(default='2021-01-01'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='in',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
        migrations.AlterField(
            model_name='out',
            name='atmosphere',
            field=models.IntegerField(choices=[(1, '⭐️'), (2, '⭐️⭐️'), (3, '⭐️⭐️⭐️'), (4, '⭐️⭐️⭐️⭐️'), (5, '⭐️⭐️⭐️⭐️⭐️')]),
        ),
        migrations.AlterField(
            model_name='out',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
        migrations.AlterField(
            model_name='out',
            name='service',
            field=models.IntegerField(choices=[(1, '⭐️'), (2, '⭐️⭐️'), (3, '⭐️⭐️⭐️'), (4, '⭐️⭐️⭐️⭐️'), (5, '⭐️⭐️⭐️⭐️⭐️')]),
        ),
        migrations.AlterField(
            model_name='out',
            name='taste',
            field=models.IntegerField(choices=[(1, '⭐️'), (2, '⭐️⭐️'), (3, '⭐️⭐️⭐️'), (4, '⭐️⭐️⭐️⭐️'), (5, '⭐️⭐️⭐️⭐️⭐️')]),
        ),
        migrations.AlterField(
            model_name='out',
            name='value',
            field=models.IntegerField(choices=[(1, '⭐️'), (2, '⭐️⭐️'), (3, '⭐️⭐️⭐️'), (4, '⭐️⭐️⭐️⭐️'), (5, '⭐️⭐️⭐️⭐️⭐️')]),
        ),
    ]
