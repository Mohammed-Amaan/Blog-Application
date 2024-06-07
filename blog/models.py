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