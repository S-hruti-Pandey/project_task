# Generated by Django 3.2.2 on 2021-06-03 08:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_alter_order_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 3, 13, 43, 56, 919748)),
        ),
    ]
