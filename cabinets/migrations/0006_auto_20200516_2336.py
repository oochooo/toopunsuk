# Generated by Django 3.0.6 on 2020-05-16 16:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabinets', '0005_auto_20200516_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cabinet',
            name='image',
            field=models.ImageField(null=True, upload_to='cabinets'),
        ),
        migrations.AlterField(
            model_name='cabinet',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 16, 23, 36, 51, 168643)),
        ),
        migrations.AlterField(
            model_name='update',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 16, 23, 36, 51, 190923)),
        ),
    ]
