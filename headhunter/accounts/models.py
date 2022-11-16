from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import TextChoices

from accounts.managers import UserManager


class RoleChoices(TextChoices):
    APPLICANT = 'applicant', 'Соискатель'
    EMPLOYER = 'employer', 'Работодатель'


class Account(AbstractUser):
    username = models.CharField(
        max_length=150,
    )
    last_name = models.CharField(
        max_length=150,
        blank=False
    )
    email = models.EmailField(
        verbose_name='Электронная почта',
        unique=True,
        blank=False,
        null=False
    )
    phone = models.CharField(
        verbose_name='Телефон',
        blank=False,
        null=False,
        max_length=15
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
    is_worker = models.BooleanField(
        null=False, 
        blank=False,
        verbose_name='Соискатель',
        default=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
