from django import forms
from .models import Post, Comment,Category
from captcha.fields import ReCaptchaField


class PostForm(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'image',
            'category',
        ]

class CommentForm(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Comment
        fields = [
            'content'
        ]

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'title'
        ]