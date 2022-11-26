from rest_framework.views import APIView

from .forms import ResumeForm, EducationForm, ExperienceForm
from .models import Resume, Education, Experience
from django.views.generic import UpdateView, CreateView, DeleteView, DetailView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse


class ResumeCreateView(CreateView):
    template_name = 'resume_create.html'
    form_class = ResumeForm
    model = Resume

    def get(self, request, *args, **kwargs):
        resume = Resume.objects.create(author=request.user)
        return redirect('resume_edit', pk=resume.pk)

    def post(self, request, *args, **kwargs):
        print('dvs')
        return super().post(request, *args, **kwargs)


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
            resume.resume_title = request.POST['resume_title']
            resume.salary = request.POST['salary']
            resume.about_yourself = request.POST['about_yourself']
            resume.email = request.POST['email']
            resume.phone = request.POST['phone']
            resume.telegram = request.POST['telegram']
            resume.linkedin = request.POST['linkedin']
            resume.facebook = request.POST['facebook']
            if len(resume.resume_title) == 0:
                del resume
                return redirect('user_detail', pk=request.user.pk)
            resume.save()
            return redirect('resume_detail', pk=resume.pk)
        context = {}
        context['form'] = form
        return render('resume_detail', pk=self.resume.pk)

    def get_success_url(self, request):
        resume = request.POST.get('id')
        print(resume)
        return reverse('resume_detail', pk=resume.pk)


class ResumeDetailView(DetailView):
    template_name = 'resume_detail.html'
    model = Resume
    context_object_name = 'resume'

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        experiences = Experience.objects.filter(resume_id=self.object.pk)
        education = Education.objects.filter(resume_id=self.object.pk)
        context['experiences'] = experiences
        context['education'] = education
        return context


class ExperienceCreateView(CreateView):
    form_class = ExperienceForm

    def post(self, request, *args, **kwargs):
        resume = Resume.objects.get(pk=kwargs['pk'])
        print("fjjfjhhfhhfdffdgfgsfg")
        print(request.POST)
        company_name = request.POST.get('company_name')
        position = request.POST.get('position')
        start_work = request.POST.get('start_work')
        end_work = request.POST.get('end_work')
        Experience.objects.create(
            company_name=company_name,
            position=position,
            start_work=start_work,
            end_work=end_work,
            resume=resume,
        )
        return HttpResponse(status=201)


class EducationCreateView(CreateView):
    from_class = EducationForm

    def post(self, request, *args, **kwargs):
        resume = Resume.objects.get(pk=kwargs['pk'])
        place_of_education = request.POST.get('place_of_education')
        specialization = request.POST.get('specialization')
        start_education = request.POST.get('start_education')
        end_education = request.POST.get('end_education')
        print(start_education)
        Education.objects.create(
            place_of_education=place_of_education,
            specialization=specialization,
            start_education=start_education,
            end_education=end_education,
            resume=resume,
        )
        return HttpResponse(status=201)
