from django.db import models
import datetime
from django.utils import timezone

# Create your models here.


class Article(models.Model):
    article_title = models.CharField(max_length=100)
    article_description = models.CharField(max_length=300)
    article = models.TextField(blank=True)
    parution_deadline = models.DateTimeField('published date')
    article_access = models.BooleanField(default=True)
