# Generated by Django 5.1.4 on 2025-01-02 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_account_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='avatar',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='avatars'),
        ),
    ]
