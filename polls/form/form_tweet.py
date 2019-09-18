from django import forms
from polls.models import Tweet

class TweetForm(forms.ModelForm):

    class TweetMeta:
        model = Tweet
        fields = ('contnet','published_date')
