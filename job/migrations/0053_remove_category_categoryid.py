# Generated by Django 4.2.6 on 2023-11-02 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0052_delete_jobapplication'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='categoryid',
        ),
    ]
