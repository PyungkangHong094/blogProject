from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone

from projectapp.models import Project


class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='article', null=True)
    slug = models.SlugField(unique=True, allow_unicode=True, null=True, blank=True)
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=False, default='')
    content = models.TextField(null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)

    like = models.IntegerField(default=0)
    
    class Meta:
        managed = False
        verbose_name = '사진'
    #
    # def __str__(self):
    #     return f'{self.writer},{self.project}'