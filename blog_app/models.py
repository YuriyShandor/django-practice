from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=75)
    author_id = models.BigIntegerField()
    content = models.TextField()
    slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default='fallback.jpg', blank=True)
