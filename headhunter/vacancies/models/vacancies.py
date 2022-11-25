from django.contrib.auth import get_user_model
from django.db import models

from resume.models.resumes import ProfessionChoices


class Vacancy(models.Model):
    author = models.ForeignKey(to=get_user_model(), verbose_name='Работодатель', related_name='author_vacancy', null=False, blank=False, on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Вакансия', max_length=100, null=False, blank=False)
    salary = models.DecimalField(verbose_name='Заработная плата', max_digits=10, decimal_places=2, null=False, blank=False)
    description = models.TextField(verbose_name='Описание вакансии', null=True)
    profession = models.CharField(verbose_name='Сфера деятельности', max_length=30, null=False, blank=False, choices=ProfessionChoices.choices)
    experience_from = models.DecimalField(verbose_name='Стаж от', max_digits=10, decimal_places=2, null=False, blank=False)
    experience_before = models.DecimalField(verbose_name='Стаж до', max_digits=10, decimal_places=2, null=False, blank=False)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата редактирования', auto_now=True)
