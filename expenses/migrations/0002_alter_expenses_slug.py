# Generated by Django 4.1.2 on 2022-10-14 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True),
        ),
    ]
