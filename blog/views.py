from django.shortcuts import render,redirect
from .models import blogPosts,blogReviews
from django.shortcuts import get_object_or_404,redirect
from .forms import BlogForm,CreateBlogForm,AddReviewForm
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

def create_blog(request):
    if request.method=='POST':
        form=CreateBlogForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/blog')
            
    else:
        form=CreateBlogForm()    
    return render(request,"create_blog.html",{"form":form})

def delete_blog(request,id):
    if request.method=='POST':
        form=blogPosts.objects.get(pk=id)
        form.delete()
        return redirect('/blog')
    
def reviews(request):
    reviews=blogReviews.objects.all()
    return render(request,'reviews.html',{'reviews':reviews})

def add_review(request):
    if request.method=="POST":
        form=AddReviewForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/blog/reviews')
    else:
        form=AddReviewForm()
    return render(request,'add_review.html',{'form':form})