from django.db import models
from django.utils.text import slugify
from django.urls import reverse
class Post(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='image',blank=True,null=True)
    content=models.TextField()
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    published_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    slug=models.SlugField(max_length=200,default='',blank=True)
    class Meta:
        ordering=['-published_at']
    
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super().save(*args,**kwargs)
    
    def get_absolute_url(self):
        return reverse('blog:detail',args=[str(self.slug)])

    def __str__(self):
        return f'{self.title}'
    
class Comment(models.Model):
    post=models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)

    class Meta:
        ordering=['created']
        indexes=[
            models.Index(fields=['created']),
            ]

    def __str__(self):
        return f'comment by {self.name} on {self.post}'
   