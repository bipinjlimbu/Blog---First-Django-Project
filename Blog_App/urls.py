from django.urls import path
from .views.main_view import index_page, create_blog, single_blog, delete_blog, edit_blog
from .views.auth_view import login_page, register_page, logout_view

urlpatterns = [
    path('', index_page, name='index'),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('logout/', logout_view, name='logout'),
    path('create-blog/', create_blog, name='create_blog'),
    path('blog/<int:id>/', single_blog, name='single_blog'),
    path('blog/edit/<int:id>/', edit_blog, name='edit_blog'),
    path('blog/delete/<int:id>/', delete_blog, name='delete_blog'),
]