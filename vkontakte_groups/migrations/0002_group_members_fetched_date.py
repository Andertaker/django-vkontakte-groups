# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vkontakte_groups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='members_fetched_date',
            field=models.DateTimeField(default=None, null=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u043f\u043e\u043b\u0443\u0447\u0435\u043d\u0438\u044f \u043f\u043e\u0434\u043f\u0438\u0441\u0447\u0438\u043a\u043e\u0432'),
            preserve_default=True,
        ),
    ]
