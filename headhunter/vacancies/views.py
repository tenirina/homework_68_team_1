from django.views.generic import CreateView


class VacancyCreateView(CreateView):
    template_name = 'resume_create.html'
    form_class = ResumeForm
    model = Resume

    def get(self, request, *args, **kwargs):
        resume = Resume.objects.create(author=request.user)
        return redirect('resume_edit', pk=resume.pk)
