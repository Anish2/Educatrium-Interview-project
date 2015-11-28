# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview_project', '0002_auto_20151126_0450'),
    ]

    operations = [
        migrations.AddField(
            model_name='element',
            name='random_num',
            field=models.IntegerField(default=4),
        ),
    ]
