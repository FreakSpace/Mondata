# Generated by Django 2.0.4 on 2018-04-05 08:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volt', models.FloatField()),
                ('amper', models.FloatField()),
                ('watt', models.FloatField()),
                ('watt_hour', models.FloatField()),
                ('dt', models.DateTimeField(default=datetime.datetime(2018, 4, 5, 11, 7, 10, 670075))),
            ],
        ),
    ]
