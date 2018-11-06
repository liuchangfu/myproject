from django import forms
from .models import Topic, Post


class NewTopicForm(forms.ModelForm):
    message = forms.CharField(label='内容',
                              widget=forms.Textarea(attrs={'rows': 5, 'placeholder': '你想输入什么呢'}),
                              max_length=40000,
                              help_text='最大长度为4000个字符', )

    class Meta:
        model = Topic
        fields = ['subject', 'message']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message', ]
