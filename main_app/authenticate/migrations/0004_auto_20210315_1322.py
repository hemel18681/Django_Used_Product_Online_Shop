# Generated by Django 3.1.7 on 2021-03-15 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0003_auto_20210314_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='user_picture',
            field=models.ImageField(blank=True, null=True, upload_to='user_images/'),
        ),
    ]
