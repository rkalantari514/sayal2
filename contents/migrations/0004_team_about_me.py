# Generated by Django 5.0.3 on 2024-03-21 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0003_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='about_me',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name=' درباره من'),
        ),
    ]
