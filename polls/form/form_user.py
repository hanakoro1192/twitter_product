from django import forms
from polls.models import User

class UserForm(forms.ModelForm):

    class UserMeta:
        model = User
        field = ('name','password')