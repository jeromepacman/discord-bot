# Generated by Django 4.0.4 on 2022-05-06 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=255, verbose_name='titre'),
        ),
    ]
