
from django import forms
from django.contrib import admin
from .models import BlogPost, Category, PostComment
# Register your models here.

admin.site.register(Category)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user','text', 'created')
admin.site.register(PostComment, CommentAdmin)


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'slug','category','views_count','comment', 'published', 'slider')
    list_editable = ('published','slider')
    exclude = ('slug','views_count','comment')
    
admin.site.register(BlogPost, BlogPostAdmin)
