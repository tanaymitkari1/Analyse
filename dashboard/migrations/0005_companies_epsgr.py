# Generated by Django 3.2.4 on 2021-06-13 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20210613_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='companies',
            name='epsgr',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
