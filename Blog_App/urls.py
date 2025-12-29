from django.urls import path
from .views.main_view import index_page
from .views.auth_view import login_page, register_page

urlpatterns = [
    path('', index_page, name='index_page'),
    path('login/', login_page, name='login_page'),
    path('register/', register_page, name='register_page'),
]