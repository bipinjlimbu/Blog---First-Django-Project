from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import Blogs
from django.contrib import messages

def index_page(request):
    blogs = Blogs.objects.all().order_by('-created_at')
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

def single_blog(request,id):
    try:
        blog = get_object_or_404(Blogs,id=id)  
        print(blog)
        return render(request,'main/single_blog.html',{'blog':blog})
    except Exception as e:
        print("Error: ",e)
    return render(request,'main/single_blog.html')

def edit_blog(request, id):
    return render(request, 'main/edit_blog.html')

def delete_blog(request, id):
    try:
        blog = get_object_or_404(Blogs,id=id)
        if blog.author == request.user:
            blog.delete()
            messages.success(request,"Blog Deleted Successfully.")
            return redirect('index')
        
        else:
            return render(request, 'main/single_blog.html',{'errors':'You are not Authorized to Delete Bro','blog':blog})

    except Exception as e:
        print(e)
