from django.urls import path
from .views.main_view import index_page
from .views.auth_view import login_page, register_page, logout_view

urlpatterns = [
    path('', index_page, name='index'),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('logout/', logout_view, name='logout'),
]