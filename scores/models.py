from django.db import models


class Score(models.Model):
    name = models.CharField("nom", max_length=200)
    points = models.IntegerField()

    def __str__(self):
        return self.name
