# Generated by Django 4.2.6 on 2023-11-01 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0034_rename_jobs_jobapplication_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobapplication',
            name='user',
        ),
    ]
