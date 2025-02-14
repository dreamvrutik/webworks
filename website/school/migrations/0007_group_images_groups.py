# Generated by Django 2.2.1 on 2020-01-24 09:24

from django.db import migrations, models
import school.models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_events_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='group_images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[(1, 2), (1, 2)], max_length=264)),
                ('image', models.ImageField(upload_to=school.models.rename_image)),
            ],
        ),
        migrations.CreateModel(
            name='groups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264)),
            ],
        ),
    ]
