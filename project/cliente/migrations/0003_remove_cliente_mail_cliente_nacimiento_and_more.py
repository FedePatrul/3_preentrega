# Generated by Django 5.0.6 on 2024-05-12 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_alter_pais_options_cliente_pais_origen_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='mail',
        ),
        migrations.AddField(
            model_name='cliente',
            name='nacimiento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='apellido',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombre',
            field=models.CharField(max_length=150),
        ),
    ]