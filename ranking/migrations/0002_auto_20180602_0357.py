# Generated by Django 2.0.5 on 2018-06-02 03:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_create_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 6, 2, 3, 57, 26, 282912, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 6, 2, 3, 57, 26, 282776, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_start_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 6, 2, 3, 57, 26, 282729, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='log',
            name='log_create_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 6, 2, 3, 57, 26, 302675, tzinfo=utc)),
        ),
    ]