# Generated by Django 4.2.6 on 2023-11-02 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0060_alter_jobapplication_cv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
