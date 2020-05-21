# Generated by Django 2.1.5 on 2020-05-16 13:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200516_1352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='time',
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
