# Generated by Django 3.2.3 on 2021-06-28 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_rename_email_reg_email1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reg',
            old_name='email1',
            new_name='email',
        ),
    ]
