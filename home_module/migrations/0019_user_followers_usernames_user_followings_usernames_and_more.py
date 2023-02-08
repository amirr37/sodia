# Generated by Django 4.0.6 on 2023-01-14 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_module', '0018_remove_post_author_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='followers_usernames',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='user',
            name='followings_usernames',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images'),
        ),
    ]
