# Generated by Django 4.0.6 on 2023-01-14 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_module', '0019_user_followers_usernames_user_followings_usernames_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='followers_usernames',
            field=models.CharField(default='username', max_length=1000),
        ),
        migrations.AlterField(
            model_name='user',
            name='followings_usernames',
            field=models.CharField(default='username', max_length=1000),
        ),
    ]