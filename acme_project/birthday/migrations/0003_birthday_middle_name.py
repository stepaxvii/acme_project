# Generated by Django 3.2.16 on 2024-05-02 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthday', '0002_auto_20240501_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='birthday',
            name='middle_name',
            field=models.CharField(blank=True, help_text='Необязательное поле', max_length=20, verbose_name='Отчество'),
        ),
    ]
