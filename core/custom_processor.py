from .models import BlogPost
from django.db.models import Q, F

def get_filter(request):
    blog_posts = BlogPost.objects.filter(published=True).order_by('-created')
    education_post = BlogPost.objects.filter(Q(published=True) & Q(category__title="Education")).order_by('-created')[:4]
    sports_post = BlogPost.objects.filter(Q(published=True) & Q(category__title="Sports")).order_by('-created')[:4]
    business_post = BlogPost.objects.filter(Q(published=True) & Q(category__title="Business")).order_by('-created')[:4]
    popular_post = BlogPost.objects.order_by(F('views_count').desc())[:6]
    
    context = {
        "blog_posts":blog_posts, 
        'education_post':education_post,
        'sports_post':sports_post,
        'business_post':business_post,
        'popular_post':popular_post
    }
    return context