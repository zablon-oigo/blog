from django.db import models

class Post(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    published_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-published_at']
    

    def __str__(self):
        return f'{self.title}-{self.author}'