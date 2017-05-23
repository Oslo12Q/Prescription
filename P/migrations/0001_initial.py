# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('image_name', models.CharField(max_length=200, blank=True)),
                ('image_json', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to=b'exhibited_picture/%Y/%m/%d')),
                ('update_time', models.DateTimeField(blank=True)),
            ],
        ),
    ]
