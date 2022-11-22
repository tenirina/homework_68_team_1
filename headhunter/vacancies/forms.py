from django import forms

from vacancies.models.vacancies import Vacancy


class ExperienceForm(forms.ModelForm):

    class Meta:
        model = Vacancy
        fields = ('title', 'salary', 'description', 'profession', 'experience_from', 'experience_before', 'updated_at')
