#from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User


#class SignupForm(UserCreationForm):
#     class Meta:
#          model = User
#          fields = ('username',)

from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from .models import User
from django import forms


class SignupForm(UserCreationForm):
     email = forms.EmailField(
        max_length=254,
        help_text='必須 有効なメールアドレスを入力してください。',
        label='Eメールアドレス'
    )
     class Meta:
          model = User
          fields = ('email', 'password1', 'password2','first_name','last_name','city','introduction','image','is_musician')