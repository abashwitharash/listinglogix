# Generated by Django 5.2 on 2025-04-08 19:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_property_status_alter_userprofile_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='date_posted',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='property',
            name='dom',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
