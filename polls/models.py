from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200)
    mailadress = models.CharField(max_length=100)


class Tweet(models.Model):
    content = models.TextField()
    published_date = models.DateTimeField(
        verbose_name='登録日',
        )
    
   # 管理サイトでの表示設定
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # def __str__(self):
    #     return self.content