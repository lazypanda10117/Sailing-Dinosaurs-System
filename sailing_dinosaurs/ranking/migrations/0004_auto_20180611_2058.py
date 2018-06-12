# Generated by Django 2.0.5 on 2018-06-11 20:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0003_auto_20180602_0952'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventactivity',
            name='event_activity_status',
            field=models.CharField(default='active', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='membergroup',
            name='membergroup_name',
            field=models.CharField(default='member_group', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='membergroup',
            name='membergroup_school',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='event_create_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 6, 11, 20, 56, 26, 306965, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 6, 11, 20, 56, 26, 306711, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_start_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 6, 11, 20, 56, 26, 306620, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='log',
            name='log_create_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 6, 11, 20, 56, 26, 322275, tzinfo=utc)),
        ),
    ]
