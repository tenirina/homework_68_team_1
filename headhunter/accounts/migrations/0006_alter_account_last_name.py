# Generated by Django 4.1.3 on 2022-11-16 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_account_worker_account_is_worker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='last_name',
            field=models.CharField(max_length=150),
        ),
    ]