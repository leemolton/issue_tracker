from django import forms
from django.forms import ModelForm
from .models import Post, Entry

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ('user', 'body', )
 
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'tag', 'published_date',)
        