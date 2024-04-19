# Generated by Django 5.0.3 on 2024-03-21 23:57

import contents.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0010_alter_projectpicture_pimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectpicture',
            name='pimage',
        ),
        migrations.AddField(
            model_name='projectpicture',
            name='pimage1',
            field=models.ImageField(blank=True, null=True, upload_to=contents.models.upload_propic_image_path, verbose_name='تصویر '),
        ),
    ]
