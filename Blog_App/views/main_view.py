from django.shortcuts import render

def index_page(request):
    return render(request, 'main/index_page.html')

def create_blog(request):
    return render(request, 'main/create_blog.html')