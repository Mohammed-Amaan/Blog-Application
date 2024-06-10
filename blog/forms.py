from django import forms
from .models import blogPosts

class BlogForm(forms.Form):
    blog_title=forms.CharField(max_length=100,label="enter blog title to search")
   


