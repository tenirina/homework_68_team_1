from django.contrib import admin
from vacancies.models.vacancies import Vacancy



class VacanсiesAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'salary', 'description', 'profession', 'experience_from', 'experience_before', 'created_at', 'updated_at')
    search_fields = ('author', 'title', 'salary', 'description', 'profession', 'experience_from', 'experience_before')
    fields = ('author', 'title', 'salary', 'description', 'profession', 'experience_from', 'experience_before')


admin.site.register(Vacancy, VacanсiesAdmin)