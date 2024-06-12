from django import forms
from .models import blogPosts,blogReviews


class BlogForm(forms.Form):
    blog_title=forms.CharField(max_length=100,label="Enter Blog Title",widget=forms.TextInput(attrs={'class': 'form-control'}))
    
class CreateBlogForm(forms.ModelForm):
    
    class Meta:
        model = blogPosts
        fields = ["title","content","author","image"]
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control','type':'file'}),
        }

class AddReviewForm(forms.ModelForm):
    blog = forms.ModelChoiceField(
        queryset=blogPosts.objects.all(), 
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    class Meta:
        model=blogReviews
        fields=['blog','comment']
        widgets={
            'comment':forms.TextInput(attrs={'class':'form-control'}),
        }
class UpdateReviewForm(forms.ModelForm):
    class Meta:
        model=blogReviews
        fields=['blog','comment']
        widgets={
            'blog':forms.TextInput(attrs={'class':'form-control'}),
            'comment':forms.TextInput(attrs={'class':'form-control'}),
        }

