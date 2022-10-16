from django.contrib.auth.models import User 
from django.utils.text import slugify
from django.utils.safestring import mark_safe
from django.db import models
import datetime
from ckeditor_uploader.fields import RichTextUploadingField



# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "1. Category"
 
 
class BlogPost(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, null=True)
    thumbnail = models.ImageField(upload_to='thumbnail')
    meta_text = models.TextField(max_length=300)
    content = RichTextUploadingField()
    published = models.BooleanField(default=False)
    slider = models.BooleanField(default=False)
    views_count = models.PositiveIntegerField(default=0)
    comment = models.PositiveIntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        original_slug = slugify(self.title)
        queryset = BlogPost.objects.all().filter(slug__iexact=original_slug).count()

        count = 1
        slug = original_slug
        while(queryset):
            slug = original_slug + '-' + str(count)
            count += 1
            queryset = BlogPost.objects.all().filter(slug__iexact=slug).count()

        self.slug = slug
        super(BlogPost, self).save(*args, **kwargs)


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = '2. Posts' 
        
    def image_tag(self):
        if self.thumbnail:
            return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.thumbnail.url)
           

class PostComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text
    
    class Meta:
        verbose_name_plural = '3. Comments' 
    