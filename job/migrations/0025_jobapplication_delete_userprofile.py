# Generated by Django 4.2.6 on 2023-10-31 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0024_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('skills', models.TextField()),
                ('cv', models.FileField(upload_to='cv_uploads/')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications_for_job', to='job.jobs')),
            ],
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]