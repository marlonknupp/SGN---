# Generated by Django 5.2.1 on 2025-06-15 18:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leasing', '0008_rename_defeito_leasing_cidade'),
    ]

    operations = [
        migrations.AddField(
            model_name='leasing',
            name='data_entrada',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='leasing',
            name='quantidade',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
