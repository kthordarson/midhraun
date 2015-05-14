# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0002_auto_20150514_1252'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='path',
            new_name='imagepath',
        ),
    ]
