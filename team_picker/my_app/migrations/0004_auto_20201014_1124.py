# Generated by Django 3.1.2 on 2020-10-14 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_auto_20201014_0745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='date_joined',
            field=models.DateTimeField(),
        ),
    ]
