from django.shortcuts import render
from .models import blogPosts
from django.shortcuts import get_object_or_404
# Create your views here.
def blog(request):
    blogs=blogPosts.objects.all()
    return render(request,"blog.html",{'blogs':blogs})

def blog_detail(request,blog_id):
    blog=get_object_or_404(blogPosts,pk=blog_id)
    return render(request,'blog_description.html',{'blog':blog})