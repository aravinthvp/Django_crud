# Generated by Django 2.0.7 on 2019-12-01 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='mobile',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='users',
            name='userid',
            field=models.CharField(max_length=15),
        ),
    ]
