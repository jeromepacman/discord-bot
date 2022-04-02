from django.db import models


class Score(models.Model):
    name = models.CharField("nom", max_length=100)
    points = models.IntegerField()
    
    def __str__(self):
        return self.name
