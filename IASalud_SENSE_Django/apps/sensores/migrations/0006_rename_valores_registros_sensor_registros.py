# Generated by Django 4.1.13 on 2024-04-08 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sensores', '0005_rename_registros_sensor_sensor_valores_registros'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sensor',
            old_name='valores_registros',
            new_name='registros',
        ),
    ]