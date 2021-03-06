# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0002_question_sort_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='text_de',
            field=models.CharField(max_length=200, null=True, verbose_name='Choice Text', blank=True),
        ),
        migrations.AddField(
            model_name='question',
            name='extra_de',
            field=models.CharField(help_text='Extra information (use  on question type)', max_length=512, null=True, verbose_name='Extra information', blank=True),
        ),
        migrations.AddField(
            model_name='question',
            name='footer_de',
            field=models.TextField(help_text=b'Footer rendered below the question interpreted as textile', null=True, verbose_name='Footer', blank=True),
        ),
        migrations.AddField(
            model_name='question',
            name='text_de',
            field=models.TextField(null=True, verbose_name='Text', blank=True),
        ),
        migrations.AddField(
            model_name='questionset',
            name='text_de',
            field=models.TextField(help_text=b"This is interpreted as Textile: <a href='http://en.wikipedia.org/wiki/Textile_%28markup_language%29' target='_blank'>http://en.wikipedia.org/wiki/Textile_(markup_language)</a>", null=True, verbose_name='Text', blank=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='Email', blank=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='language',
            field=models.CharField(default=b'en', max_length=2, verbose_name='Language', choices=[(b'en', b'English'), (b'de', b'Deutsch')]),
        ),
    ]
