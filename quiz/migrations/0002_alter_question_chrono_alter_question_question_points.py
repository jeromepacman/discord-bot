# Generated by Django 4.0.3 on 2022-04-02 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='chrono',
            field=models.IntegerField(verbose_name='Temps max'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_points',
            field=models.SmallIntegerField(verbose_name='points'),
        ),
    ]
