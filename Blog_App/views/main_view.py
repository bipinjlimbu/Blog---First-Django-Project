from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index_page(request):
    return render(request, 'main/index_page.html')

@login_required
def create_blog(request):
    return render(request, 'main/create_blog.html')