from django import forms
from .models import Experience, Resume, Education



class ResumeForm(forms.ModelForm):

    class Meta:
        model = Resume
        widgets = {
            'about_yourself': forms.Textarea(attrs={'cols': 21, 'rows': 5}),
        }
        fields = ('resume_title', 'salary', 'profession', 'phone', 'email', 'about_yourself', 'telegram', 'linkedin', 'facebook', 'publication')

class ExperienceForm(forms.ModelForm):

    class Meta:
        model = Experience
        fields = ('company_name', 'position', 'start_work', 'end_work')

class EducationForm(forms.ModelForm):

    class Meta:
        model = Education
        fields = ('place_of_education', 'specialization', 'start_education', 'end_education')
