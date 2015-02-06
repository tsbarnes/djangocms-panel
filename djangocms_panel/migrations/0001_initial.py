# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Panel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('context', models.CharField(default=b'panel-default', max_length=25, choices=[(b'panel-default', b'Default'), (b'panel-primary', b'Primary'), (b'panel-success', b'Success'), (b'panel-info', b'Info'), (b'panel-warning', b'Warning'), (b'panel-danger', b'Danger')])),
                ('title', models.CharField(max_length=100, null=True, blank=True)),
                ('footer', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
