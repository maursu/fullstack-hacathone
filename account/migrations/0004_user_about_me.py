# Generated by Django 4.1.6 on 2023-02-19 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_user_is_fireman_user_is_mentor'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='about_me',
            field=models.TextField(default='modest user'),
        ),
    ]
