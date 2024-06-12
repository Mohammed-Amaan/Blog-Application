from django.shortcuts import render,redirect
from .models import blogPosts,blogReviews
from django.shortcuts import get_object_or_404,redirect
from .forms import BlogForm,CreateBlogForm,AddReviewForm,UpdateReviewForm
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
# Create your views here.

#display all blogs
@login_required(login_url='/user/login')
def blog(request):
    blogs=blogPosts.objects.all()
    return render(request,"blog.html",{'blogs':blogs})
#display blog description
def blog_detail(request,blog_id):
    blog=get_object_or_404(blogPosts,pk=blog_id)
    return render(request,'blog_description.html',{'blog':blog})
#search for a blog and display details
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

#create a blog
@login_required(login_url='/user/login')
def create_blog(request):
    if request.method=='POST':
        form=CreateBlogForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/blog')
    else:
        form=CreateBlogForm()    
    return render(request,"create_blog.html",{"form":form})

#delete blog
def delete_blog(request,id):
    if request.method=='POST':
        form=blogPosts.objects.get(pk=id)
        form.delete()
        return redirect('/blog')

#display all reviews
@login_required(login_url='/user/login')
def reviews(request):
    reviews=blogReviews.objects.all()
    return render(request,'reviews.html',{'reviews':reviews})

#add review
def add_review(request):
    if request.method=="POST":
        form=AddReviewForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/blog/reviews')
    else:
        form=AddReviewForm()
    return render(request,'add_review.html',{'form':form})

#update review
def update_review(request,id):
    if request.method=="POST":
        review=blogReviews.objects.get(pk=id)
        review.date_added=timezone.now()
        form=UpdateReviewForm(request.POST,instance=review)
        if form.is_valid():
            form.save()
            return redirect('/blog/reviews')
    else:
        review=blogReviews.objects.get(pk=id)
        form=AddReviewForm(instance=review)

    return render(request,'update_review.html',{'form':form})
