# Generated by Django 4.2.6 on 2023-10-29 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
