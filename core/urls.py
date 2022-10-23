from django.urls import path
# from django_summernote.views import (SummernoteEditor, SummernoteUploadAttachment)
from .views import home, post_detail, category_list, user_login, user_signup,  change_password, user_logout, load_posts

urlpatterns = [
    path('', home, name="home"),
    path('read/<int:id>/', post_detail, name="post_detail"),
    path('category_list/<int:id>/', category_list, name='category_list'),
    path('signup/', user_signup, name="user_signup"),
    path('login/', user_login, name="user_login"),
    path('change-password/', change_password, name="change_password"),
    path('logout/', user_logout, name="user_logout"),
    path('load-post', load_posts, name="load_posts")
]
