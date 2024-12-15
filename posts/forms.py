from lib2to3.fixes.fix_input import context

from django import forms
from django.template.defaultfilters import title

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'rate', 'category', 'tags')

    def clean_title(self):
        title = self.cleaned_data['title']
        if "python" in title.lower():
            raise forms.ValidationError("Title must not contain python")
        return title

    def clean_content(self):
        content = self.cleaned_data['content']
        if len(content) < 5:
            raise forms.ValidationError("Content must contain more than 5 characters")
        return content

    def clean(self):
        data = super().clean()
        title = data.get("title")
        content = data.get("content")
        if title == content:
            raise forms.ValidationError("Title and content must be different")
        return data