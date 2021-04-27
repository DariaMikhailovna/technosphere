from django import forms
from .models import Chat


class ChatForm(forms.ModelForm):

    class Meta:
        model = Chat
        fields = ['title', 'created_date', 'author', 'participants']
