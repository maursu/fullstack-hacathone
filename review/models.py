from django.db import models
from django.contrib.auth import get_user_model
from slugify import slugify

from questions.models import Question


User = get_user_model()


class Answer(models.Model):
    body = models.TextField()
    image = models.ImageField(upload_to='images/answers/', blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.body


class Comment(models.Model):
    body = models.TextField()
    comment = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.body