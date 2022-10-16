from django.urls import path
# from django_summernote.views import (SummernoteEditor, SummernoteUploadAttachment)
from .views import home, post_detail, post_list, user_login, user_signup,  change_password, user_logout

urlpatterns = [
    path('', home, name="home"),
    path('read/<slug>/', post_detail, name="post_detail"),
    path('post_list/', post_list, name='post_list'),
    path('signup/', user_signup, name="user_signup"),
    path('login/', user_login, name="user_login"),
    path('change-password/', change_password, name="change_password"),
    path('logout/', user_logout, name="user_logout"),
]
