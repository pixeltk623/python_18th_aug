# Generated by Django 3.2.7 on 2021-12-17 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='city',
            field=models.CharField(default=True, max_length=255),
        ),
        migrations.AddField(
            model_name='person',
            name='gender',
            field=models.CharField(default=True, max_length=255),
        ),
        migrations.AddField(
            model_name='person',
            name='hobby',
            field=models.CharField(default=True, max_length=255),
        ),
    ]
