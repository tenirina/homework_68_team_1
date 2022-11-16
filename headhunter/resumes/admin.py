from django.contrib import admin
from resumes.models import Resume



class ResumeAdmin(admin.ModelAdmin):
    list_display = ('id', 'resume_title', 'salary', 'profession', 'phone', 'email', 'about_yourself', 'telegram', 'linkedin', 'facebook')
    search_fields = ('resume_title', 'salary', 'profession', 'phone', 'email', 'about_yourself', 'telegram', 'linkedin', 'facebook')
    fields = ('resume_title', 'salary', 'profession', 'phone', 'email', 'about_yourself', 'telegram', 'linkedin', 'facebook')


admin.site.register(Resume, ResumeAdmin)