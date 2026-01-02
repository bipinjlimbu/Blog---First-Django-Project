from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models import Blogs
from django.contrib import messages

def index_page(request):
    blogs = Blogs.objects.all()
    return render(request, 'main/index_page.html',{'blogs':blogs})

@login_required
def create_blog(request):
    error = {}
    if request.method == 'POST':
        title = request.POST.get('title')
        category = request.POST.get('category')
        content = request.POST.get('content')
        image = request.FILES.get('image')

        if not title:
            error['title'] = 'Title is required.'

        if not category:
            error['category'] = 'Category is required.'

        if not content:
            error['content'] = 'Content is required.'

        if error:
            return render(request, 'main/create_blog.html', {'error': error, 'data': request.POST})

        try:
            blog = Blogs(
                title=title,
                category=category,
                content=content,
                image=image,
                author=request.user,
            )
            blog.save()
            messages.success(request, 'Blog created successfully!')
            return redirect('index')
        
        except Exception as e:
            print(e)
            return render(request, 'main/create_blog.html', {'error[general]': 'An error occurred while creating the blog. Please try again.', 'data': request.POST})
            
    return render(request, 'main/create_blog.html')