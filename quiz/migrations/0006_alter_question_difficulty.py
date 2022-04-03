# Generated by Django 4.0.3 on 2022-04-02 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_alter_answer_options_alter_answer_answer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='difficulty',
            field=models.IntegerField(choices=[(0, '-----'), (1, 'Noob'), (2, 'Medium'), (3, 'Advanced'), (4, 'Hero')], default=0, verbose_name='niveau'),
        ),
    ]