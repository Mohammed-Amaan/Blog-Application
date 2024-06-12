from django.urls import path
from . import views
urlpatterns = [
    path('',views.blog,name="blog"),
    path('<int:blog_id>/',views.blog_detail,name='blog_details'),
    path('search',views.search_blog,name='blog_Search'),
    path('create',views.create_blog,name='create_blogs'),
    path('<int:id>delete/',views.delete_blog,name='delete_blog'),
    path('reviews',views.reviews,name="reviews"),
    path('reviews/add',views.add_review,name="add_review"),
    path('reviews/update/<int:id>/',views.update_review,name='update_review'),

]
