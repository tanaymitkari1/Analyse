# Generated by Django 3.2.4 on 2021-06-14 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20210614_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companies',
            name='pe1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
