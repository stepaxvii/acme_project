from django.views.generic import (
     CreateView,
     DeleteView,
     DetailView,
     ListView,
     UpdateView
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .forms import BirthdayForm
from .models import Birthday
from .utils import calculate_birthday_countdown


class OnlyAuthorMixin(UserPassesTestMixin):

    def test_func(self):
        object = self.get_object()
        return object.author == self.request.user


class BirthdayListView(ListView):
    model = Birthday
    ordering = 'id'
    paginate_by = 5


class BirthdayUpdateView(LoginRequiredMixin, OnlyAuthorMixin, UpdateView):
    model = Birthday
    form_class = BirthdayForm


class BirthdayCreateView(LoginRequiredMixin, CreateView):
    model = Birthday
    form_class = BirthdayForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BirthdayDeleteView(LoginRequiredMixin, OnlyAuthorMixin, DeleteView):
    model = Birthday
    success_url = reverse_lazy('birthday:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        birthday = self.get_object()
        context['birthday'] = birthday
        return context


class BirthdayDetailView(DetailView):
    model = Birthday
    success_url = reverse_lazy('birthday:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['birthday_countdown'] = calculate_birthday_countdown(
            self.object.birthday
        )
        return context


@login_required
def simple_view(request):
    return HttpResponse('Страница для залогиненных пользователей!')
