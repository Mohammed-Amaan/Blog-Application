from django.contrib import admin
from .models import blogPosts,blogReviews
# Register your models here.
class BlogReviewInline(admin.TabularInline):
    model=blogReviews
    extra=1
'''
class BlogAdmin(admin.ModelAdmin):
    inlines = [BlogReviewInline]
'''
class BlogReviewAdmin(admin.ModelAdmin):
    list_display=("blog","comment",)
admin.site.register(blogPosts)
admin.site.register(blogReviews,BlogReviewAdmin)
