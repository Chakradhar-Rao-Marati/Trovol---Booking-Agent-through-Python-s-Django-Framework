# Generated by Django 5.0.2 on 2024-03-17 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trovol', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
