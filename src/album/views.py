# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response

from album.models import Image


def list_all(request):
    albums = {}
    for image in Image.objects.all():
        key = 'Óflokkað'
        if image.horse:
            key = image.horse.name
        albums.setdefault(key, []).append(image)
    return render_to_response('album.html', {'albums': albums})
