# Generated by Django 3.1.7 on 2021-04-20 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0006_user_info_user_card_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_info',
            name='user_card_number',
        ),
    ]