# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('random_header', models.CharField(max_length=200)),
                ('random_text', models.CharField(max_length=200)),
                ('random_popup_title', models.CharField(max_length=200)),
                ('random_popup_text', models.CharField(max_length=200)),
            ],
        ),
    ]
