# -*- coding: utf-8 -*-
from datetime import datetime
from django.shortcuts import render_to_response
from django.contrib.auth.models import User

from horses.models import Horse, Log


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
