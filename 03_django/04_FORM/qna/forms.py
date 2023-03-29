from django import forms
from .models import Question


class QuestionForm(forms.ModelForm):
    
    reward = forms.IntegerField(min_value=1, max_value=100)

    class Meta:
        model = Question
        fields = '__all__'