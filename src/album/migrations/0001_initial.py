# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('horses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('path', models.FilePathField(verbose_name=b'/media/datadrive/forritun/Python/midhraun/uploads')),
                ('horse', models.ForeignKey(to='horses.Horse', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
