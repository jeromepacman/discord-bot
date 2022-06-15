from django.db import models


class Question(models.Model):
    LEVEL = (
        (0,  "-----"),
        (1, "Noob"),
        (2, "Medium"),
        (3, "Advanced"),
        (4, "Hero")
    )

    title = models.CharField("titre", max_length=255)
    question_points = models.IntegerField("points")
    difficulty = models.IntegerField("niveau", choices=LEVEL, default=0)
    chrono = models.IntegerField("Temps max")
    is_active = models.BooleanField("active", default=True)
    created_at = models.DateTimeField("création", auto_now_add=True)
    updated_at = models.DateTimeField("Mise à jour", auto_now=True)

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name="answer", verbose_name="Question", on_delete=models.CASCADE)
    answer = models.CharField("réponse", max_length=100)
    is_correct = models.BooleanField("correcte", default=False)
    is_active = models.BooleanField("active", default=True)
    created_at = models.DateTimeField("création", auto_now_add=True)
    updated_at = models.DateTimeField("mise à jour", auto_now=True)

    class Meta:
        verbose_name = "Réponse"

    def __str__(self):
        return self.answer


class Score(models.Model):
    name = models.CharField("nom", max_length=100)
    points = models.IntegerField("points", default=0)

    def __str__(self):
        return self.name