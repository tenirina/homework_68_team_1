from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import TextChoices


class ProfessionChoices(TextChoices):
    IT = 'IT', 'IT'
    FINANCE = 'finance', 'Финансы'
    TRADING = 'trading', 'Торговля'


class Resume(models.Model):

    author = models.ForeignKey(
        to=get_user_model(),
        verbose_name='Автор резюме',
        related_name='author',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    resume_title = models.CharField(
        max_length=300,
        verbose_name='Наименование должности',
        null=False,
        blank=False
    )
    salary = models.DecimalField(
        max_digits=10,
        verbose_name='Заработная плата',
        decimal_places=2,
        null=True,
        blank=False
    )
    profession = models.CharField(
        max_length=30, 
        null=True, 
        blank=False, 
        choices=ProfessionChoices.choices, 
        verbose_name='Сфера деятельности'
    )
    phone = models.CharField(
        verbose_name='Телефон',
        blank=True,
        null=False,
        max_length=15
    )
    email = models.EmailField(
        verbose_name='Электронная почта',
        blank=False,
        null=False
    )
    about_yourself = models.TextField(
        max_length=3000,
        verbose_name='О себе',
        null=True,
        blank=False
    )
    telegram = models.CharField(
        max_length=100,
        null=True,
        blank=False,
        verbose_name='Telegram'
    )
    linkedin = models.CharField(
        max_length=100,
        null=True,
        blank=False,
        verbose_name='LinkedIn'
    )
    facebook = models.CharField(
        max_length=100,
        null=True,
        blank=False,
        verbose_name='Facebook'
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата редактирования',
        auto_now=True
    )

    def __str__(self):
        return f'{self.author} - {self.resume_title}'