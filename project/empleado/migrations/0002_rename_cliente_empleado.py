# Generated by Django 5.0.6 on 2024-05-13 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cliente',
            new_name='Empleado',
        ),
    ]
