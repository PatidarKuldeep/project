# Generated by Django 4.2.6 on 2023-10-30 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0015_alter_category_categoryname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='categoryname',
            field=models.CharField(max_length=100),
        ),
    ]
