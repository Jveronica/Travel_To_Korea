# Generated by Django 2.2.3 on 2019-07-24 04:39

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('maps', '0002_auto_20190724_1327'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='bookmark',
            unique_together={('user', 'inform')},
        ),
        migrations.AlterUniqueTogether(
            name='comment',
            unique_together={('user', 'inform')},
        ),
        migrations.AlterUniqueTogether(
            name='score',
            unique_together={('user', 'inform')},
        ),
        migrations.AlterUniqueTogether(
            name='stamp',
            unique_together={('user', 'inform')},
        ),
    ]
