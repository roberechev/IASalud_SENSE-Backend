# Generated by Django 4.1.13 on 2024-04-04 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0001_initial'),
        ('sensores', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensor',
            name='ultimo_registro',
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='valor',
        ),
        migrations.AddField(
            model_name='sensor',
            name='valores',
            field=models.ManyToManyField(to='registros.registro'),
        ),
    ]