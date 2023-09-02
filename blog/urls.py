from django.urls import path
from .views import *
app_name='blog'

urlpatterns=[
        path('post/<slug:slug>/',BlogDetailView.as_view(),name='detail'),
    path('',BlogListView.as_view(), name='home'),

]