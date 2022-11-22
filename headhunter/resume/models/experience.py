from django.db import models


class Experience(models.Model):

    company_name = models.CharField(
        max_length=150,
        blank=False,
        null=False,
        verbose_name='Наименование компании'
    )
    position = models.CharField(
        max_length=150,
        blank=False,
        null=False,
        verbose_name='Должность'
    )
    start_work = models.DateField(
        verbose_name='Дата начала работы',
        null=False,
        blank=False
    )
    end_work = models.DateField(
        verbose_name='Дата окончания работы',
        null=False,
        blank=False
    )
    resume = models.ForeignKey(
        to='resume.Resume',
        related_name='resume_exp',
        null=False,
        blank=False,
        verbose_name='Резюме',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.company_name} - {self.position}'