# Generated by Django 3.2.4 on 2021-06-13 08:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='companies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_name', models.CharField(blank=True, max_length=100, null=True)),
                ('industry', models.CharField(blank=True, max_length=100, null=True)),
                ('cmp', models.IntegerField()),
                ('date', models.CharField(blank=True, max_length=100, null=True)),
                ('eps1', models.IntegerField()),
                ('eps2', models.IntegerField()),
                ('eps3', models.IntegerField()),
                ('eps4', models.IntegerField()),
                ('eps5', models.IntegerField()),
                ('eps6', models.IntegerField()),
                ('eps7', models.IntegerField()),
                ('eps8', models.IntegerField()),
                ('eps9', models.IntegerField()),
                ('cpe', models.IntegerField()),
                ('ipe', models.IntegerField()),
                ('pe1', models.IntegerField()),
                ('pe2', models.IntegerField()),
                ('pe3', models.IntegerField()),
                ('pe4', models.IntegerField()),
                ('pe5', models.IntegerField()),
                ('pe6', models.IntegerField()),
                ('pe7', models.IntegerField()),
                ('pe8', models.IntegerField()),
                ('pe9', models.IntegerField()),
                ('bv', models.IntegerField()),
                ('der', models.IntegerField()),
                ('fcf', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
