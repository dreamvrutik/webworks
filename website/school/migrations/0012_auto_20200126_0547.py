# Generated by Django 3.0.2 on 2020-01-26 05:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0011_auto_20200126_0540'),
    ]

    operations = [
        migrations.AddField(
            model_name='approach',
            name='details',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='events',
            name='details',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
