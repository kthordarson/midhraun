# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='path',
            field=models.FilePathField(path=b'/media/datadrive/forritun/Python/midhraun/uploads'),
            preserve_default=True,
        ),
    ]
