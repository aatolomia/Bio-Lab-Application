# Generated by Django 2.1.6 on 2019-04-25 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0009_auto_20190425_1338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrow',
            name='item',
        ),
        migrations.RemoveField(
            model_name='borrow',
            name='qty',
        ),
        migrations.RemoveField(
            model_name='borrow',
            name='status',
        ),
        migrations.RemoveField(
            model_name='pending',
            name='num_borrowed',
        ),
        migrations.AddField(
            model_name='borrow',
            name='name_item',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
