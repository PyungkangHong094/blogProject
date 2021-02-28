from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article

class LikeRecord(models.Model):
    # 주인이 없어지면 다 없어지도록
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like_record')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='like_record')

    # 좋아요는 하나만
    class Meta:
        unique_together = ('user', 'article')
