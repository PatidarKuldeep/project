# Generated by Django 4.2.6 on 2023-10-29 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]