# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-02-17 15:52
from __future__ import unicode_literals

from django.db import migrations, models


def migrate_settings(apps, schema_editor):
    SettingValue = apps.get_model('core', 'SettingValue')
    SettingValueTranslation = apps.get_model('core', 'SettingValueTranslation')

    translations = SettingValueTranslation.objects.all()

    for translation in translations:
        setting = SettingValue.objects.get(pk=translation.master_id)
        setattr(setting, 'value_{}'.format(translation.language_code), translation.hvad_value)
        setting.save()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0046_delete_review_request_sent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='settingvaluetranslation',
            old_name='value',
            new_name='hvad_value',
        ),
        migrations.AddField(
            model_name='settingvalue',
            name='value',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='settingvalue',
            name='value_cy',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='settingvalue',
            name='value_de',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='settingvalue',
            name='value_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='settingvalue',
            name='value_fr',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.RunPython(migrate_settings, reverse_code=migrations.RunPython.noop),
    ]
