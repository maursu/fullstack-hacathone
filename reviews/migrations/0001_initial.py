# Generated by Django 4.1.6 on 2023-02-13 11:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('answers', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionReview',
            fields=[
                ('id',
                 models.BigAutoField(
                     auto_created=True,
                     primary_key=True,
                     serialize=False,
                     verbose_name='ID')),
                ('is_liked',
                 models.BooleanField(
                     default=False)),
                ('author',
                 models.ForeignKey(
                     on_delete=django.db.models.deletion.CASCADE,
                     related_name='question_reviews',
                     to=settings.AUTH_USER_MODEL)),
                ('question',
                 models.ForeignKey(
                     on_delete=django.db.models.deletion.CASCADE,
                     related_name='question_reviews',
                     to='questions.question')),
            ],
        ),
        migrations.CreateModel(
            name='AnswerReview',
            fields=[
                ('id',
                 models.BigAutoField(
                     auto_created=True,
                     primary_key=True,
                     serialize=False,
                     verbose_name='ID')),
                ('is_liked',
                 models.BooleanField(
                     default=False)),
                ('answer',
                 models.ForeignKey(
                     on_delete=django.db.models.deletion.CASCADE,
                     related_name='answer_reviews',
                     to='answers.answer')),
                ('author',
                 models.ForeignKey(
                     on_delete=django.db.models.deletion.CASCADE,
                     related_name='answer_reviews',
                     to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
