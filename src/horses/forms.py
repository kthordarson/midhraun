# -*- coding: utf-8 -*-
from django import forms
from horses.models import Parent, Category


class HorseForm(forms.Form):
    name = forms.CharField(label='Nafn', max_length=255)
    color = forms.CharField(label='Litur', max_length=255)
    owner = forms.CharField(label='Eigandi', max_length=255)
    breeder = forms.CharField(label='Ræktandi', max_length=255)
    birthdate = forms.DateField(label='Fæðingardagur',
                                input_formats=['%d.%m.%Y'])
    identity = forms.CharField(label='Kennitala', max_length=255)
    father = forms.ModelChoiceField(label='F',
                                    queryset=Parent.objects.all(),
                                    empty_label='-- Velja --')
    mother = forms.ModelChoiceField(label='M',
                                    queryset=Parent.objects.all(),
                                    empty_label='-- Velja --')
    category = forms.ModelChoiceField(label='Flokkur',
                                      queryset=Category.objects.all(),
                                      empty_label=None)
    # TODO: images
