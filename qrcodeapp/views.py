# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Qrdata

# Create your views here.
def index(request):
    data = Qrdata.objects.all()

    context = {
        'qrdata':data,
    }

    return render(request, 'index.html', {'data':data})
