# Generated by Django 4.1.6 on 2023-02-15 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('answers', '0002_alter_answer_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='image',
            field=models.ImageField(blank=True, upload_to='answers/'),
        ),
    ]