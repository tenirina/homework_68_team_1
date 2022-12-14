# Generated by Django 4.1.2 on 2022-11-23 17:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Вакансия')),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Заработная плата')),
                ('description', models.TextField(null=True, verbose_name='Описание вакансии')),
                ('profession', models.CharField(choices=[('IT', 'IT'), ('finance', 'Финансы'), ('trading', 'Торговля')], max_length=30, verbose_name='Сфера деятельности')),
                ('experience_from', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Стаж от')),
                ('experience_before', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Стаж до')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL, verbose_name='Работодатель')),
            ],
        ),
    ]
