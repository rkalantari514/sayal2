# Generated by Django 5.0.3 on 2024-03-22 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0015_services_discription1_services_discription2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='discription',
        ),
        migrations.RemoveField(
            model_name='services',
            name='name',
        ),
    ]
