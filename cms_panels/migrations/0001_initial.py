# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-04 12:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('filer', '0007_auto_20161016_1055'),
    ]

    operations = [
        migrations.CreateModel(
            name='Panel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='cms_panels_panel', serialize=False, to='cms.CMSPlugin')),
                ('css_class', models.CharField(blank=True, default='', max_length=200, verbose_name='CSS class')),
                ('in_navigation', models.BooleanField(default=False, verbose_name='In navigation')),
                ('is_visible', models.BooleanField(default=True, verbose_name='Visible')),
                ('height', models.CharField(blank=True, default='', max_length=100, verbose_name='Height')),
                ('width', models.CharField(blank=True, default='', max_length=50, verbose_name='Width')),
                ('name', models.CharField(blank=True, default='', max_length=150, verbose_name='Name')),
                ('slug', models.SlugField(blank=True, default='', editable=False, max_length=150, verbose_name='Slug')),
                ('cms_page', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cms_pictures_picture_set', to='cms.Page')),
                ('filer_image', filer.fields.image.FilerImageField(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cms_pictures_picture_set', to='filer.Image', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Panel ',
                'verbose_name_plural': 'Panels',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='PanelInfo',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='cms_panels_panelinfo', serialize=False, to='cms.CMSPlugin')),
                ('name', models.CharField(blank=True, default='', max_length=150, verbose_name='Name')),
                ('coord_x', models.PositiveIntegerField(blank=True, default='50', verbose_name='X coordinat')),
                ('coord_y', models.PositiveIntegerField(blank=True, default='50', verbose_name='Y coordinat')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
