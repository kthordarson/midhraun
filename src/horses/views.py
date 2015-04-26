# -*- coding: utf-8 -*-
from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf

from horses.models import Horse, Log
from horses.forms import HorseForm


def log(request, horse_id):
    horse = Horse(name='Brá')
    log = [Log(date=datetime.now(),
               user=User.objects.get(username='admin'),
               description="Stuttur reiðtúr - hoppar aðeins upp á fótinn "
                           "hægra meginn en hætti ef hvatt er á vinstri "
                           "afturfót og hún sveigð aðeins til hægri. Góður "
                           "höfuðburður á tölti en ekki mjúk/róleg - vill "
                           "alltaf fara hraðar. Höfuðburður á brokki "
                           "sæmilegur en þarf vinnu. Slær aðeins saman á "
                           "brokkinu.")]
    log[0].category = "Ýmislegt"
    log[0].details = "Ýmislegt"
    log[0].results = "Ýmislegt"
    return render_to_response('log.html', {'horse': horse, 'log': log})


def new_horse(request):
    if request.method == "POST":
        if request.POST.get('cancel'):
            return HttpResponseRedirect(reverse('ui.views.home'))
        form = HorseForm(request.POST)
        if form.is_valid():
            # TODO: save new horse
            return HttpResponseRedirect(reverse('ui.views.home'))
    else:
        form = HorseForm()
    ctx = {'form': form}
    ctx.update(csrf(request))
    return render_to_response('horseform.html', ctx)
