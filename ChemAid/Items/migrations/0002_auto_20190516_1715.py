# Generated by Django 2.1.7 on 2019-05-16 09:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Items', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2019, 5, 23, 17, 15, 53, 896177)),
        ),
    ]
