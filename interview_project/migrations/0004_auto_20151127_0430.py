# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview_project', '0003_element_random_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='random_num',
            field=models.IntegerField(default=2),
        ),
    ]
