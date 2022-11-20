from django.contrib import admin
from resumes.models import Resume, Experience, Education

class ExperienceInline(admin.StackedInline):
    model = Experience
    fields = ('company_name', 'position', 'start_work', 'end_work')

class EducationInline(admin.StackedInline):
    model = Education
    fields = ('place_of_education', 'specialization', 'start_education', 'end_education')


class ResumeAdmin(admin.ModelAdmin):
    inlines = (ExperienceInline, EducationInline, )
    # list_display = ('id', 'resume_title', 'salary', 'profession', 'phone', 'email', 'about_yourself', 'telegram', 'linkedin', 'facebook')
    # search_fields = ('resume_title', 'salary', 'profession', 'phone', 'email', 'about_yourself', 'telegram', 'linkedin', 'facebook')
    # fields = ('resume_title', 'salary', 'profession', 'phone', 'email', 'about_yourself', 'telegram', 'linkedin', 'facebook')


admin.site.register(Resume, ResumeAdmin)