# Generated by Django 4.1.6 on 2023-02-13 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_github_account_user_is_recognized_member_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
    ]
