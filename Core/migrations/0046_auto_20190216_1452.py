# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2019-02-16 09:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0045_auto_20190122_0933'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='codechef_handle',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='codechef_team_name',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='second_branch',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='second_codechef_handle',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='second_contact',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='second_email',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='second_gender',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='second_hosteler',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='second_name',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='second_student_number',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='second_university_rollno',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='second_year',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='university_rollno',
        ),
    ]
