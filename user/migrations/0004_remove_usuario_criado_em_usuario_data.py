# Generated by Django 5.2.3 on 2025-06-26 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_remove_usuario_notebook'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='criado_em',
        ),
        migrations.AddField(
            model_name='usuario',
            name='data',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
