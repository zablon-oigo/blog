from django.urls import path
from .views import *
app_name='blog'

urlpatterns=[
    path('',BlogListView.as_view(), name='home'),
    path('detail/<slug:slug>/',BlogDetailView.as_view(),name='detail'),
]