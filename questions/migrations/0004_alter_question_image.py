# Generated by Django 4.1.6 on 2023-02-15 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_rename_views_question_views_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/questions/'),
        ),
    ]