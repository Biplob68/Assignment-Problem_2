# Generated by Django 3.2.3 on 2021-06-27 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(default='', max_length=111)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
