# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

# Описание полей таблицы, в которой будут хранится журнальные записи
class Record(models.Model):

    date = models.DateField(
        auto_now_add=True,
    )
    text = models.CharField(
        max_length=255,
    )
# Вывод текстовыми строками
    def __str__(self):
        return ' '.join([
            str(self.date),
            self.text,
        ])

