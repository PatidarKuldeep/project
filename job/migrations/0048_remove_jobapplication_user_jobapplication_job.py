# Generated by Django 4.2.6 on 2023-11-02 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0047_rename_job_jobapplication_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobapplication',
            name='user',
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='job',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='applications_for_job', to='job.jobs'),
            preserve_default=False,
        ),
    ]
