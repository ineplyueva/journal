# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Record(models.Model):

    date = models.DateField(
        auto_now_add=True,
    )
    text = models.CharField(
        max_length=1255,
    )
    def __str__(self):
        return ' '.join([
            self.date,
            self.text,
        ])

