# Generated by Django 4.2.6 on 2023-10-30 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0016_alter_category_categoryname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobs',
            name='job_category',
        ),
        migrations.RemoveField(
            model_name='jobs',
            name='job_subcategory',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Jobs',
        ),
    ]
