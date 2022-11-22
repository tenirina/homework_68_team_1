from django.db import models

from resumes.models.resumes import ProfessionChoices


class Vacancy(models.Model):

    title = models.CharField(verbose_name='Вакансия', max_length=100, null=False, blank=False)
    salary = models.DecimalField(verbose_name='Заработная плата', max_length=10, decimal_places=2, null=False, blank=False)
    description = models.TextField(verbose_name='Описание вакансии', null=True)
    profession = models.CharField(verbose_name='Сфера деятельности', max_length=30, null=False, blank=False, choices=ProfessionChoices.choices)
    experience_from = models.DecimalField(verbose_name='Стаж от', max_length=10, decimal_places=2, null=False, blank=False)
    experience_before = models.DecimalField(verbose_name='Стаж до', max_length=10, decimal_places=2, null=False, blank=False)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата редактирования', auto_now=True)
