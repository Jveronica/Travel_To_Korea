# Generated by Django 2.2.3 on 2019-08-07 01:05

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('maps', '0002_auto_20190806_1338'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='comment',
            unique_together={('id', 'user', 'contentId')},
        ),
    ]
