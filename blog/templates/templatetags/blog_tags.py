from django import template
from models import Post
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown
# creating a simple tag to return a string of the number of articles published
register=template.Library()
@register.simple_tag
def total_post():
    return Post.count()

# Creating an inclusion tag to show the latest Post redered using a template
@register.inclusion_tag('templates/blog/latest_post.html')
def show_latest_post(count=5):
    latest_post=Post.order_by('-published_at')[:count]
    return {'latest_post':latest_post}

# Create a template that return a Queryset for the most commented Post
@register.simple_tag
def get_most_commented_post(count=5):
    return Post.annotate(
        total_comments=Count('comments')
    ).order_by('-total_comments')[:count]

# creating a template filter to support markdown syntax
@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))
