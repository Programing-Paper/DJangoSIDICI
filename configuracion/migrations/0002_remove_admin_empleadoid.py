# Generated by Django 4.1.1 on 2023-01-26 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='empleadoid',
        ),
    ]
