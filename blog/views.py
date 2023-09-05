from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Post
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import PostForm
class BlogListView(ListView):
    model=Post
    template_name='blog/index.html'
    context_object_name='posts'


class BlogDetailView(DetailView):
    model=Post
    template_name='blog/post_detail.html'

class CreateBlogView(CreateView):
    form_class=PostForm
    template_name='blog/create.html'
   
    def form_valid(self, form):
        form.instance.author=self.request.user
        messages.success(self.request,'The post was created successfully')
        return super(CreateBlogView,self).form_valid(form)

class BlogUpdateView(UpdateView):
    model=Post
    form_class=PostForm
    template_name='blog/update_post.html'
    # success_url=reverse_lazy('blog:home')

    def form_valid(self,form):
        messages.success(self.request,"The post was updated successfully")
        return super(BlogUpdateView,self).form_valid(form)

class DeleteBlogView(DeleteView):
    model=Post
    template_name='blog/delete_post.html'
    success_url=reverse_lazy('blog:home')

    def form_valid(self,form):
        messages.success(self.request,'The post has been deleted successfully')
        return super(DeleteBlogView,self).form_valid(form)

