# Generated by Django 3.2.18 on 2023-03-25 03:07

from django.db import migrations, models
import pathlib


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_extracciones_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='configFile',
            field=models.FilePathField(blank=True, null=True, path=pathlib.PureWindowsPath('D:/GitHub/FullStack_Github/SmartDebt-copy/app'), verbose_name='Lectura BSS'),
        ),
    ]