# Generated by Django 2.1.7 on 2019-03-29 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipment',
            name='is_favorite',
        ),
    ]
