# Generated by Django 5.1.4 on 2025-01-02 13:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_account_groups_account_user_permissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='date_joined',
            field=models.DateTimeField(verbose_name=datetime.datetime(2025, 1, 2, 13, 45, 49, 958752, tzinfo=datetime.timezone.utc)),
        ),
    ]
