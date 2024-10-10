# Generated by Django 5.1.1 on 2024-10-10 05:18

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_alter_event_options_alter_eventimage_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventuser',
            name='branch',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='رشته تحصیلی'),
        ),
        migrations.AddField(
            model_name='eventuser',
            name='student_number',
            field=models.CharField(default=django.utils.timezone.now, max_length=20, verbose_name='شماره دانشجویی'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='eventuser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='شماره تلفن'),
        ),
    ]