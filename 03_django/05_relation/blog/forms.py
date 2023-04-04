# blog/forms.py
from django import forms
from .models import Posting, Reply


class PostingForm(forms.ModelForm):

    class Meta:
        model = Posting
        # user 빼고 모든 필드 다
        exclude = ('user', )


class ReplyForm(forms.ModelForm):

    class Meta:
        model = Reply
        # content 필드만
        fields = ('content', )
        # exclude = ('posting', )