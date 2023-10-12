from django.contrib import admin
from .models import Post,Comment

admin.site.register(Post)

@admin.register(Comment)
class AdminComment(admin.ModelAdmin):
    list_display=['name','post','created','is_active']
    list_filter=['is_active','created','updated']
    search_fields=['name','body']