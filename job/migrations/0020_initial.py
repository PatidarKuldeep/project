# Generated by Django 4.2.6 on 2023-10-30 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('job', '0019_remove_jobs_job_category_remove_jobs_job_subcategory_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryid', models.IntegerField()),
                ('categoryname', models.CharField(max_length=100)),
                ('subcategoryname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=100)),
                ('job_description', models.CharField(max_length=1000)),
                ('job_location', models.CharField(max_length=100)),
                ('job_experience', models.CharField(max_length=100)),
                ('job_salary', models.CharField(max_length=100)),
                ('job_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs_in_category', to='job.category')),
                ('job_subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs_in_subcategory', to='job.category')),
            ],
        ),
    ]
