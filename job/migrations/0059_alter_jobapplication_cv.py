# Generated by Django 4.2.6 on 2023-11-02 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0058_alter_jobapplication_cv_alter_jobapplication_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='cv',
            field=models.FileField(blank=True, upload_to='cv_uploads/'),
        ),
    ]
