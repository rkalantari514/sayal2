# Generated by Django 5.0.3 on 2024-03-23 11:08

import contents.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0021_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='فعال / غیر فعال')),
                ('name', models.CharField(max_length=150, verbose_name='نام گواهینامه')),
                ('gimage', models.ImageField(blank=True, null=True, upload_to=contents.models.upload_grade_path, verbose_name='تصویر ')),
            ],
            options={
                'verbose_name': 'گواهینامه',
                'verbose_name_plural': 'گواهینامه ها',
            },
        ),
    ]
