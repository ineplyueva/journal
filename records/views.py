# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from django.views.generic import CreateView
from django.core.urlresolvers import reverse
from records.models import Record

# Настройка вывода журнала
class RecordsView(ListView):

    model = Record
    template_name = 'journal.html'

# Настройка создания новой записи
class AddRecord(CreateView):
    model = Record
    template_name = 'add_record.html'
    fields = ['text']
    def get_success_url(self):
        return reverse('journal')
