# Generated by Django 4.1.13 on 2024-04-08 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sensores', '0004_rename_registros_sensor_registros_sensor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sensor',
            old_name='registros_sensor',
            new_name='valores_registros',
        ),
    ]
