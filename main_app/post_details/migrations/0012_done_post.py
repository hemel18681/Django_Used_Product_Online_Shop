# Generated by Django 3.1.7 on 2021-04-19 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_details', '0011_auto_20210412_1658'),
    ]

    operations = [
        migrations.CreateModel(
            name='done_post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_phone_number', models.IntegerField()),
                ('post_title', models.CharField(max_length=100)),
                ('post_description', models.TextField()),
                ('post_picture', models.ImageField(upload_to='post_images/')),
                ('post_money', models.DecimalField(decimal_places=2, max_digits=20)),
                ('post_used_days', models.IntegerField(default=0)),
                ('done_post', models.BooleanField(default=False)),
                ('post_given_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
