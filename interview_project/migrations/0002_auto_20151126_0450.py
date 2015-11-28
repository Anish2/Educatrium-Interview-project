# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview_project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='random_popup_text',
            field=models.CharField(max_length=1000),
        ),
    ]
