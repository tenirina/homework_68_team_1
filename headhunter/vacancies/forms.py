from django import forms
from resume.models import Resume
from vacancies.models.vacancies import Vacancy, ResponseToVacancy


class VacancyForm(forms.ModelForm):

    class Meta:
        model = Vacancy
        fields = ('title', 'salary', 'description', 'profession', 'experience_from', 'experience_before')


class VacancyResponceForm(forms.ModelForm):
    def __init__(self, current_user, *args, **kwargs):
        super(VacancyResponceForm, self).__init__(*args, **kwargs)
        self.fields['resume'].queryset = self.fields['resume'].queryset.filter(author=current_user.pk)

    resume = forms.ModelChoiceField(
        label='Необходимо выбрать резюме',
        queryset=Resume.objects.all(),
    )
    class Meta:
        model = ResponseToVacancy
        fields = ('resume', )


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='')