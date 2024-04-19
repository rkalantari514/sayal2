# Generated by Django 5.0.3 on 2024-03-21 21:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0007_alter_projects_about_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='area',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='مساحت'),
        ),
        migrations.AddField(
            model_name='projects',
            name='employer',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='کارفرما'),
        ),
        migrations.AddField(
            model_name='projects',
            name='engineer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contents.team', verbose_name='مهندس پروژه'),
        ),
        migrations.AddField(
            model_name='projects',
            name='kinde',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='نوع پوژه'),
        ),
        migrations.AddField(
            model_name='projects',
            name='locationp',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='محل پروژه'),
        ),
        migrations.AddField(
            model_name='projects',
            name='price',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='مبلغ پروژه'),
        ),
        migrations.AddField(
            model_name='projects',
            name='statusp',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='وضعیت'),
        ),
        migrations.AddField(
            model_name='projects',
            name='timep',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='زمان پروژه'),
        ),
        migrations.AddField(
            model_name='projects',
            name='zirbana',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='زیر بنا'),
        ),
    ]
