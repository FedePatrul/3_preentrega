# Generated by Django 5.0.6 on 2024-05-12 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_remove_cliente_mail_cliente_nacimiento_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='nacimiento',
        ),
        migrations.AddField(
            model_name='cliente',
            name='mail',
            field=models.CharField(default=50, max_length=150),
            preserve_default=False,
        ),
    ]
