# Generated by Django 5.2.1 on 2025-06-04 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notebook',
            name='categoria',
        ),
        migrations.AddField(
            model_name='notebook',
            name='quantidade',
            field=models.IntegerField(default=0),
        ),
    ]
