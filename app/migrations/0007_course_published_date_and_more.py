# Generated by Django 5.1.4 on 2025-01-03 07:30

import datetime
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_enrolledcourse_enrollment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='enrolledcourse',
            name='enrollment_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2025, 1, 3, 7, 29, 58, 770876, tzinfo=datetime.timezone.utc)),
        ),
    ]
