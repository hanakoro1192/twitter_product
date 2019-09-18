from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    name = models.CharField(verbose_name='タイトル', max_length=100)
    email = models.CharField(max_length=100)
    password = models.TextField(blank=False, null=False)
    

class Tweet(models.Model):
    content = models.TextField(verbose_name='内容')
    published_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.content