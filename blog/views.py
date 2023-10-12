from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Post
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import PostForm, CommentForm
from django.views.decorators.http import require_POST
class BlogListView(ListView):
    model=Post
    template_name='blog/index.html'
    context_object_name='posts'


class BlogDetailView(LoginRequiredMixin,DetailView):
    model=Post
    template_name='blog/post_detail.html'

class CreateBlogView(LoginRequiredMixin,CreateView):
    form_class=PostForm
    template_name='blog/create.html'
   
    def form_valid(self, form):
        form.instance.author=self.request.user
        messages.success(self.request,'The post was created successfully')
        return super(CreateBlogView,self).form_valid(form)

class BlogUpdateView(LoginRequiredMixin,UpdateView):
    model=Post
    form_class=PostForm
    template_name='blog/update_post.html'
    # success_url=reverse_lazy('blog:home')

    def form_valid(self,form):
        messages.success(self.request,"The post was updated successfully")
        return super(BlogUpdateView,self).form_valid(form)

class DeleteBlogView(LoginRequiredMixin,DeleteView):
    model=Post
    template_name='blog/delete_post.html'
    success_url=reverse_lazy('blog:home')

    def form_valid(self,form):
        messages.success(self.request,'The post has been deleted successfully')
        return super(DeleteBlogView,self).form_valid(form)

@require_POST
def post_comment(request, post_id):
    post=get_object_or_404(Post, id=post_id)
    comment=None
    form=CommentForm(data=request.POST)
    if form.is_valid():
        comment=form.save(commit=False)
        comment.post=post
        comment.name=request.user.username
        comment.save()
    return render(request,'blog/comment.html',{'post':post,'form':form,'comment':comment})
