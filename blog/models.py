from django.db import models
from django.utils import timezone
# Create your models here.
class blogPosts(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    image=models.ImageField(upload_to='blogs/')
    date_added=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
#one to many relationship 
class blogReviews(models.Model):
    blog=models.ForeignKey(blogPosts,on_delete=models.CASCADE,related_name='reviews')
    comment=models.TextField()
    date_added=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'review for {self.blog}'