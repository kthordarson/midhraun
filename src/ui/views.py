# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from horses.models import Category, Horse


def index(request):
    return render_to_response('index.html')


def home(request):
    cat = Category(name='Graðhestar')
    horse = Horse(name="Þeyr")
    categories = {
        cat.name: {
            'horses': [horse, Horse(name="Álfhildur")]
        },
        "Ræktunarmerar Íslandi": {
            'horses': [Horse(name="Álfadrottning frá Austurkoti")]
        }
    }
    return render_to_response('home.html', {'categories': categories})


def categories(request):
    from django.http import HttpResponse
    return HttpResponse()
