# Generated by Django 2.2.1 on 2020-01-24 09:38

from django.db import migrations, models
import django.db.models.deletion
import school.models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0009_auto_20200124_1505'),
    ]

    operations = [
        migrations.CreateModel(
            name='groups',
            fields=[
                ('group_name', models.CharField(max_length=264, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='group_images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=school.models.rename_image)),
                ('group_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.groups')),
            ],
        ),
    ]
