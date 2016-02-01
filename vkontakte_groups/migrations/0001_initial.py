# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import m2m_history.fields
import vkontakte_api.models


class Migration(migrations.Migration):

    dependencies = [
        ('vkontakte_users', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('fetched', models.DateTimeField(db_index=True, null=True, verbose_name='\u041e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u043e', blank=True)),
                ('remote_id', models.BigIntegerField(help_text='\u0423\u043d\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440', serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=800)),
                ('screen_name', models.CharField(max_length=50, verbose_name='\u041a\u043e\u0440\u043e\u0442\u043a\u043e\u0435 \u0438\u043c\u044f \u0433\u0440\u0443\u043f\u043f\u044b', db_index=True)),
                ('is_closed', models.NullBooleanField(verbose_name='\u0424\u043b\u0430\u0433 \u0437\u0430\u043a\u0440\u044b\u0442\u043e\u0439 \u0433\u0440\u0443\u043f\u043f\u044b')),
                ('is_admin', models.NullBooleanField(verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c \u044f\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440\u043e\u043c')),
                ('members_count', models.IntegerField(null=True, verbose_name='\u0412\u0441\u0435\u0433\u043e \u0443\u0447\u0430\u0441\u0442\u043d\u0438\u043a\u043e\u0432')),
                ('verified', models.NullBooleanField(verbose_name='\u0424\u043b\u0430\u0433 \u043e\u0444\u0438\u0446\u0438\u0430\u043b\u044c\u043d\u043e\u0439 \u0433\u0440\u0443\u043f\u043f\u044b')),
                ('type', models.CharField(max_length=10, verbose_name='\u0422\u0438\u043f \u043e\u0431\u044a\u0435\u043a\u0442\u0430', choices=[(b'group', '\u0413\u0440\u0443\u043f\u043f\u0430'), (b'page', '\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430'), (b'event', '\u0421\u043e\u0431\u044b\u0442\u0438\u0435')])),
                ('photo', models.URLField()),
                ('photo_big', models.URLField()),
                ('photo_medium', models.URLField()),
                ('members', m2m_history.fields.ManyToManyHistoryField(related_name='members_groups', to='vkontakte_users.User')),
            ],
            options={
                'verbose_name': 'Vkontakte group',
                'verbose_name_plural': 'Vkontakte groups',
            },
            bases=(vkontakte_api.models.RemoteIdModelMixin, models.Model),
        ),
    ]
