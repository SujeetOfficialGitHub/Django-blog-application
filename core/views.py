
from unicodedata import category
from django.shortcuts import redirect, render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.db.models import Q, F
from core.models import BlogPost, PostComment
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Home page 
def home(request):
    sliders = BlogPost.objects.filter(Q(published=True) & Q(slider=True)).order_by('-id')[:4]
    context = {
        "sliders":sliders,
    }
    return render(request, 'core/index.html',context=context)

# Load more posts 
def load_posts(request):
    post_count = int(request.GET['post'])
    limit = 4
    blog_posts = BlogPost.objects.filter(published=True).order_by('-created')[post_count:post_count+limit]
    t = render_to_string('ajax/load-posts.html', {'blog_posts':blog_posts})
    return JsonResponse({'blog_posts':t})

# Post detaii page 
def post_detail(request, id):
    post = get_object_or_404(BlogPost, id=id)
    post_comment = request.POST.get("comment")
    if request.user:
        if post_comment:
            user_comment = PostComment(
                user = request.user,
                post = post,
                text = post_comment
            )
            user_comment.save()
            
    comments = PostComment.objects.filter(post=post)
    comment_count = PostComment.objects.filter(post=post).count()
    
    # post views count 
    post.views_count += 1
    post.comment = comment_count
    post.save()
    
    
    context={
        "post":post,
        "comments":comments,
        "comment_count":comment_count
    }
    return render(request, 'core/detail.html', context=context)

# Show all posts 
def category_list(request, id):
    posts = BlogPost.objects.filter(Q(published=True) & Q(category=id)).order_by('-id')
    return render(request, 'core/category-list.html',{'posts':posts})

# user signup form 
def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            return render(request, 'core/signup.html', {'form':form})
    else:
        form = UserCreationForm()
        return render(request, 'core/signup.html', {'form':form})
    
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            return render(request, 'core/login.html', {'form':form})
    else:
        form = AuthenticationForm()
        return render(request, 'core/login.html', {'form':form})
    
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
           form.save()
           update_session_auth_hash(request, form.user)
           return redirect('home')
        else:
            return render(request, 'core/password_change_form.html',{'form':form})       
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request, 'core/password_change_form.html',{'form':form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('home')