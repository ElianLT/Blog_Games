# Generated by Django 4.1.6 on 2023-03-12 01:04

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nucleo', '0002_about_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='icon',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Icono'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='Contenido'),
        ),
    ]
