from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.db import models
from ckeditor.fields import RichTextField



class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class News(models.Model):
    class Status(models.TextChoices):
        Draft = 'DF', 'Draft'
        Published = 'PB', 'Publish'

    class News(models.Model):
        views = models.PositiveIntegerField(default=0)

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = RichTextField()
    image = models.ImageField(upload_to='news/images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publish_time = models.DateTimeField(default=timezone.now)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.Draft
    )



    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_detail', args=[self.slug])


class Photos(models.Model):
    image = models.ImageField(upload_to='photos/images')


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)


    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.user} {self.news} {self.body}"