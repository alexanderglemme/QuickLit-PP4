# Generated by Django 3.2.18 on 2023-05-26 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0015_auto_20230526_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversationmessage',
            name='conversation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='marketplace.conversation'),
        ),
    ]