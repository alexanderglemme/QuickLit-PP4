# Generated by Django 3.2.18 on 2023-04-23 14:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0004_alter_salesad_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesad',
            name='created_on',
            field=models.DateTimeField(default=datetime.date.today),
        ),
    ]
