# Generated by Django 4.0.4 on 2022-05-06 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='points',
            field=models.PositiveIntegerField(verbose_name='points'),
        ),
    ]
