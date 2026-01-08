from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import Blogs
from django.contrib import messages

def index_page(request):
    blogs = Blogs.objects.all().order_by('-created_at')
    featured = Blogs.objects.filter(is_featured = 1).order_by('-created_at')
    return render(request, 'main/index_page.html',{'blogs':blogs,'featured':featured})

@login_required
def create_blog(request):
    error = {}
    if request.method == 'POST':
        title = request.POST.get('title')
        category = request.POST.get('category')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        is_featured = request.POST.get('is_featured') == 'on'

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
                is_featured=is_featured
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

@login_required
def edit_blog(request, id):
    error = {}
    blog = get_object_or_404(Blogs,id=id)

    if blog.author != request.user and not request.user.is_superuser:
        return redirect('single_blog',blog.id)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        category = request.POST.get('category')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        is_featured = request.POST.get('is_featured') == 'on'

        if not title:
            error['title'] = 'Title is required.'

        if not category:
            error['category'] = 'Category is required.'

        if not content:
            error['content'] = 'Content is required.'

        if error:
            return render(request, 'main/edit_blog.html', {'error': error, 'blog': blog})
        
        blog.title = title
        blog.category = category
        blog.content = content
        blog.is_featured = is_featured
        
        if image:
            blog.image = image

        blog.save()
        messages.success(request,'Blog Updated Successfully.')
        return redirect('single_blog',blog.id)

    return render(request, 'main/edit_blog.html',{'blog':blog})

@login_required
def delete_blog(request, id):
    try:
        blog = get_object_or_404(Blogs,id=id)
        if blog.author == request.user or request.user.is_superuser:
            blog.delete()
            messages.success(request,"Blog Deleted Successfully.")
            return redirect('index')
        
        else:
            return render(request, 'main/single_blog.html',{'errors':'You are not Authorized to Delete Bro','blog':blog})

    except Exception as e:
        print(e)
