from django.contrib import admin

from . import models


class AnswerInlineModel(admin.TabularInline):
    model = models.Answer
    fields = ['answer', 'is_correct']


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = ['title', 'difficulty', 'question_points', 'chrono']
    list_display = ['title', 'difficulty',
                    'question_points', 'updated_at', 'is_active']
    inlines = [AnswerInlineModel, ]
    filter_by = ['title', 'difficulty']


@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['answer', 'is_correct', 'question']
