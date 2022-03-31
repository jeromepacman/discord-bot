from django.db import models


class Question(models.Model):
    LEVEL = (
        (0, 'choisir'),
        (1, 'Noobs'),
        (2, 'Medium'),
        (3, 'Advanced'),
        (4, 'Hero')
    )

    title = models.CharField("titre", max_length=200)
    points = models.SmallIntegerField()
    difficulty = models.IntegerField("Difficulté", choices=LEVEL, default=0)
    chrono = models.IntegerField(default=8)
    is_active = models.BooleanField("Active", default=True)
    created_at = models.DateTimeField("création", auto_now_add=True)
    updated_at = models.DateTimeField("Mise à jour", auto_now=True)

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answer', verbose_name= "Question", on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)
    is_correct = models.BooleanField("Correct", default=False)
    is_active = models.BooleanField("Active", default=True)
    created_at = models.DateTimeField("création", auto_now_add=True)
    updated_at = models.DateTimeField("Mise à jour", auto_now=True)

    def __str__(self):
        return self.answer
