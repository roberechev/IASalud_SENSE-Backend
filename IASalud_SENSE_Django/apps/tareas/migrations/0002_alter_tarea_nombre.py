# Generated by Django 4.1.13 on 2024-03-21 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='nombre',
            field=models.TextField(blank=True),
        ),
    ]