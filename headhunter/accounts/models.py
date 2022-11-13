from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import TextChoices


class RoleChoices(TextChoices):
    WORKER = 'worker', 'Работадатель'
    EMPLOYER = 'employer', 'Соискатель'


class Account(AbstractUser):
    email = models.EmailField(
        verbose_name='Электронная почта',
        unique=True,
        blank=False,
        null=False
    )

    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to='avatars',
        verbose_name='Аватар'
    )

    birthday = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата рождения'
    )

    worker = models.CharField(
        max_length=30, 
        null=False, 
        blank=False, 
        choices=RoleChoices.choices, 
        verbose_name='Тип'
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
