# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview_project', '0006_element_element_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='element_id',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]
