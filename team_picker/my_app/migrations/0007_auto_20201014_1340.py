# Generated by Django 3.1.2 on 2020-10-14 13:40

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('my_app', '0006_auto_20201014_1126'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='membership',
            unique_together={('player', 'team')},
        ),
    ]