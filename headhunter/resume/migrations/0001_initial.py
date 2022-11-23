# Generated by Django 4.0 on 2022-11-22 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0007_alter_account_groups_alter_account_user_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume_title', models.CharField(max_length=300, null=True, verbose_name='Наименование должности')),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Заработная плата')),
                ('profession', models.CharField(choices=[('IT', 'IT'), ('finance', 'Финансы'), ('trading', 'Торговля')], max_length=30, null=True, verbose_name='Сфера деятельности')),
                ('phone', models.CharField(blank=True, max_length=15, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('about_yourself', models.TextField(max_length=3000, null=True, verbose_name='О себе')),
                ('telegram', models.CharField(max_length=100, null=True, verbose_name='Telegram')),
                ('linkedin', models.CharField(max_length=100, null=True, verbose_name='LinkedIn')),
                ('facebook', models.CharField(max_length=100, null=True, verbose_name='Facebook')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author', to='accounts.account', verbose_name='Автор резюме')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=150, verbose_name='Наименование компании')),
                ('position', models.CharField(max_length=150, verbose_name='Должность')),
                ('start_work', models.DateField(verbose_name='Дата начала работы')),
                ('end_work', models.DateField(verbose_name='Дата окончания работы')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resume_exp', to='resume.resume', verbose_name='Резюме')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_of_education', models.CharField(max_length=150, verbose_name='Место обучения')),
                ('specialization', models.CharField(max_length=150, verbose_name='Специальность')),
                ('start_education', models.DateField(verbose_name='Дата начала обучения')),
                ('end_education', models.DateField(verbose_name='Дата окончания обучения')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resume_edu', to='resume.resume', verbose_name='Резюме')),
            ],
        ),
    ]