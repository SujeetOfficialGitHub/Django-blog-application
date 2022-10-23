
from .models import BlogPost, Category
from django.db.models import Q, F

def get_filter(request):
    latest_post = BlogPost.objects.filter(published=True).order_by('-created')
    blog_posts = BlogPost.objects.filter(published=True).order_by('-created')[:4]
    total_post = BlogPost.objects.filter(published=True).count()
    categories = BlogPost.objects.filter(published=True).distinct().values('category__title', 'category__id')
    
    popular_post = BlogPost.objects.order_by(F('views_count').desc())[:6]
    
    context = {
        'categories':categories,
        "latest_post":latest_post, 
        'blog_posts':blog_posts,
        'popular_post':popular_post,
        'total_post':total_post,
    }
    return context