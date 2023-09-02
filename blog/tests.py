from django.test import TestCase,Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Post

class BlogTest(TestCase):

    def setUp(self):
        self.user=get_user_model().objects.create_user(

            username='testuser',
            email='test@email.com',
            password='secret'
        )

        self.post=Post.objects.create(
            
            title='A good title',
            content='Nice body content',
            author=self.user,
        )
    
    def test_string_representation(self):
        post=Post(title='A sample title')
        self.assertEqual(str(post),post.title)
    
    def test_post_content(self):
        self.assertEqual(f'{self.post.title}','A good title')
        self.assertEqual(f'{self.post.author}','testuser')
        self.assertEqual(f'{self.post.content}','Nice body content')
    
    def test_post_list_view(self):
        response=self.client.get(reverse('blog:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,'Nice body content')
        self.assertTemplateUsed(response,'blog/index.html')
    
    def test_post_detail_view(self):
        response = self.client.get('/post/<slug:slug>/')
        no_response=self.client.get('/detail/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response,'A good title')
        self.assertTemplateUsed(response,'blog/post_detail.html')



