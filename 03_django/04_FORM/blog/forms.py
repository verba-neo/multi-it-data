from django import forms
from .models import Student

# 2. Views에서 입력 <=> 필드 직접 매칭 귀찮
# 1. 사용자 입력의 유효성 검증(Validation)
# 3. HTML에서 input 태그 생성 귀찮


class StudentForm(forms.ModelForm):
    name = forms.CharField(min_length=2, max_length=20)
    age = forms.IntegerField(min_value=19, max_value=100)
    balance = forms.IntegerField(min_value=0)
    
    class Meta:
        model = Student
        # fields에 적힌 필드만 검증/HTML 해줌
        # fields = ('name', 'age', 'balance', )
        # exclude = ('mbti', )
        fields = '__all__'
