from resumes.forms import ResumeForm, EducationForm, ExperienceForm
from resumes.models import Resume, Education, Experience
from django.views.generic import UpdateView, CreateView, DeleteView, DetailView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect, get_object_or_404



class ResumeCreateView(CreateView):
    template_name = 'resume_create.html'
    form_class = ResumeForm
    model = Resume

    def get(self, request, *args, **kwargs):
        resume = Resume.objects.create(author=request.user)
        return redirect('resume_edit', pk=resume.pk)


class ResumeEditView(UpdateView):
    template_name = 'resume_edit.html'
    model = Resume
    form_class = ResumeForm
    context_object_name = 'resume'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ResumeForm(instance=self.object)
        context['form_exp'] = ExperienceForm()
        context['form_edu'] = EducationForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            resume = get_object_or_404(Resume, pk=kwargs.get('pk'))
            resume.save()
            return redirect('profile', pk=self.request.user.pk)
        context = {}
        context['form'] = form
        return render('profile', pk=self.request.user.pk)

    def get_success_url(self, request):
        return reverse('profile', kwargs={'pk': self.object.author})