from django.db import models


class Score(models.Model):
    name = models.CharField("nom", max_length=128)
    points = models.PositiveIntegerField('points')

    def __str__(self):
        return self.name