# Generated by Django 3.2.18 on 2023-05-05 13:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0013_auto_20230505_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
