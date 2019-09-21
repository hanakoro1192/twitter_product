from django.shortcuts import render
from django.utils import timezone
from .models import User, Tweet
# from .form_user import UserForm
# from .form_tweet import TweetrForm

# ホームの画面
def twitter(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    content = {'tweets' : tweets }
    return render(request, 'twitter/base.html', content)

# 登録画面するときの画面
def user_view(request):
    return render(request, 'twitter/register.html')

#投稿画面
def tweet_view(request):
    return render(request, 'twitter/post.html')