# Generated by Django 4.1.13 on 2024-04-25 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='edad',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='paciente',
            name='genero',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='paciente',
            name='nombre',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
