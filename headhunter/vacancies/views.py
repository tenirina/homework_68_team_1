from django.shortcuts import redirect
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from django.urls import reverse
from vacancies.forms import VacancyForm, SearchForm
from vacancies.models.vacancies import Vacancy



class VacancyListView(ListView):
    template_name = 'vacancies.html'
    model = Vacancy
    context_object_name = 'vacancies'

    def get(self, request, *args, **kwargs):
        self.form = SearchForm(self.request.GET)
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data.get('search')
        return None

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = Vacancy.objects.filter(title__icontains=self.search_value)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['form'] = self.form
        return context


class VacancyCreateView(CreateView):
    template_name = 'vacancies_create.html'
    form_class = VacancyForm
    model = Vacancy

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author_id = request.user.pk
            form.save()
            return redirect('user_detail', pk=request.user.pk)
        context = {}
        context['form'] = form
        return self.render_to_response(context)

    def get_success_url(self, request):
        return reverse('user_detail', pk=request.user.pk)


class VacancyEditView(UpdateView):
    template_name = 'vacancies_edit.html'
    form_class = VacancyForm
    model = Vacancy
    context_object_name = 'vacancy'

    def get_context_data(self, **kwargs):
        context = super(VacancyEditView, self).get_context_data(**kwargs)
        context['form'] = VacancyForm(instance=self.object)
        return context

    def get_success_url(self):
        return reverse('vacancy_detail', kwargs={'pk': self.object.pk})


class VacancyDetailView(DetailView):
    template_name = 'vacancies_detail.html'
    model = Vacancy
    context_object_name = 'vacancy'
