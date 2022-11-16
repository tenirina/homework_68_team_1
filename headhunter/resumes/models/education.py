from django.db import models



class Education(models.Model):

    place_of_education = models.CharField(
        max_length=150,
        blank=False,
        null=False,
        verbose_name='Место обучения'
    )
    specialization = models.CharField(
        max_length=150,
        blank=False,
        null=False,
        verbose_name='Специальность'
    )
    start_education = models.DateField(
        verbose_name='Дата начала обучения',
        null=False,
        blank=False
    )
    end_education = models.DateField(
        verbose_name='Дата окончания обучения',
        null=False,
        blank=False
    )
    resume = models.ForeignKey(
        to='resumes.Resume',
        related_name='resume_edu',
        null=False,
        blank=False,
        verbose_name='Резюме',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.place_of_education} - {self.specialization}'