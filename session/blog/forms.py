from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        # Meta : 클래스 내부에서 그 클래스를 재정의
        model = Blog
        # 사용할 모델은 Blog 클래스
        fields = ['title', 'content']
        # 사용할 필드는 Blog 클래스의 fields
