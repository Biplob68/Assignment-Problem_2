# Generated by Django 3.2.3 on 2021-06-28 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_auto_20210628_1418'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reg',
            name='f_name',
        ),
        migrations.RemoveField(
            model_name='reg',
            name='l_name',
        ),
    ]
