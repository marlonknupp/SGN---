# Generated by Django 5.2.1 on 2025-06-15 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leasing', '0009_leasing_data_entrada_leasing_quantidade'),
    ]

    operations = [
        migrations.AddField(
            model_name='leasing',
            name='observações',
            field=models.CharField(blank=True, null=True),
        ),
    ]
