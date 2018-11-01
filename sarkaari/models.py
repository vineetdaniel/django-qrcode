# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import qrcode

# Create your models here.
class Tax(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    ward_no = models.PositiveIntegerField()
    ward_name = models.CharField(max_length=200)
    record_created = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        data = self.clean_fields

        t = Tax
        img = qrcode.make('some data here')
        img.save('C:\\Users\\2200002708\\Documents\qr.png')
        super(Tax, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

