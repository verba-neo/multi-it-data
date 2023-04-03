# blog/forms.py
from django import forms
from .models import Posting, Reply


class PostingForm(forms.ModelForm):

    class Meta:
        model = Posting
        fields = '__all__'


class ReplyForm(forms.ModelForm):

    class Meta:
        model = Reply
        fields = '__all__'