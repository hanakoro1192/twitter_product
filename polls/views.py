from django.shortcuts import render
from django.utils import timezone
from .models import User, Tweet
# from .form_user import UserForm
# from .form_tweet import TweetrForm

# ホームの画面
def polls(request):
    Tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'polls/base.html')

# 登録画面するときの画面
def UseView(request):
    return render(request, 'polls/register.html')

#投稿画面
def TweetView(request):
    return render(request, 'polls/Posthtml')