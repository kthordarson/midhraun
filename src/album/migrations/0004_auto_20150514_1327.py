# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0003_auto_20150514_1253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='imagepath',
        ),
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.ImageField(default=1, upload_to=b'/media/datadrive/forritun/Python/midhraun/uploads'),
            preserve_default=False,
        ),
    ]
