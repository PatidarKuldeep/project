# Generated by Django 4.2.6 on 2023-10-30 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0014_alter_jobs_job_category_alter_jobs_job_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='categoryname',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]