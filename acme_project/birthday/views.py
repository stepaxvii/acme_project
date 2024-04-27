from django.shortcuts import render

from .forms import BirthdayForm


def birthday(request):
    form = BirthdayForm()
    return render(request, 'birthday/birthday.html', {'form': form})