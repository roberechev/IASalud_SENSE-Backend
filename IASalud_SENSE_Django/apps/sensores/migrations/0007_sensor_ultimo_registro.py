# Generated by Django 4.1.13 on 2024-04-10 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensores', '0006_rename_valores_registros_sensor_registros'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='ultimo_registro',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
