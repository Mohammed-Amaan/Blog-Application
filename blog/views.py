from django.shortcuts import render
from .models import blogPosts
from django.shortcuts import get_object_or_404
from .forms import BlogForm
# Create your views here.
def blog(request):
    blogs=blogPosts.objects.all()
    return render(request,"blog.html",{'blogs':blogs})

def blog_detail(request,blog_id):
    blog=get_object_or_404(blogPosts,pk=blog_id)
    return render(request,'blog_description.html',{'blog':blog})

def search_blog(request):
    blog=None
    if request.method=='POST':
        form=BlogForm(request.POST) 
        if form.is_valid():
            blog_title=form.cleaned_data['blog_title']
            blog=blogPosts.objects.filter(title=blog_title)
    else:
        form=BlogForm()
    return render(request,'search_blog.html',{'blog':blog,'form':form})