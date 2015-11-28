# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview_project', '0005_remove_element_random_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='element',
            name='element_id',
            field=models.IntegerField(default=0),
        ),
    ]
