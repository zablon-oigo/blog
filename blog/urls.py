from django.urls import path
from .views import *
app_name='blog'

urlpatterns=[
    path('',BlogListView.as_view(), name='home'),
    path('create/',CreateBlogView.as_view(), name='create'),
    path('delete/<int:pk>/',DeleteBlogView.as_view(),name='delete'),
    path('update/<int:pk>/',BlogUpdateView.as_view(), name='update'),
    path('post/<slug:slug>/',BlogDetailView.as_view(),name='detail'),
    path('<int:post_id>/comment/',post_comment, name='post_comment'),
    

]