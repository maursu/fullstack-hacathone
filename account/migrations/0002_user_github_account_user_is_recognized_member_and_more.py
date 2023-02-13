# Generated by Django 4.1.6 on 2023-02-13 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='github_account',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_recognized_member',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='telegram_account',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='user_photo',
            field=models.ImageField(blank=True, upload_to='media/account/'),
        ),
        migrations.AddField(
            model_name='user',
            name='web_site',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]