# Generated by Django 4.0.6 on 2023-01-01 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_module', '0005_user_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=''),
        ),
    ]