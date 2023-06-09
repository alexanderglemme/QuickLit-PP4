# Generated by Django 3.2.18 on 2023-05-05 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0012_conversation_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='conversation',
            options={'ordering': ['-updated_at']},
        ),
        migrations.RemoveField(
            model_name='conversation',
            name='slug',
        ),
        migrations.AddField(
            model_name='conversation',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
