# Generated by Django 4.2.6 on 2023-10-30 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0022_remove_jobs_job_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='job_description',
            field=models.TextField(),
        ),
    ]
