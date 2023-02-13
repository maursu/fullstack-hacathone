from django.db import models
from django.contrib.auth import get_user_model
from slugify import slugify


User = get_user_model()

class Tag(models.Model):
    title = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=20, primary_key=True, blank=True)
    description = models.CharField(max_length=40)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()

    def __str__(self) -> str:
        return self.title


class Question(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, primary_key=True, blank=True)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')
    image = models.ImageField(upload_to='images/questions/', blank=True)
    tag = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()

    def __str__(self) -> str:
        return self.title
