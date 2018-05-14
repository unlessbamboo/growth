# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-19 10:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='age',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(
                blank=True,
                max_length=254,
                verbose_name='e-mail'),
        ),
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(
                default='bamboo',
                max_length=30,
                verbose_name='\u540d'),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=40, verbose_name='\u6027'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publication_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
