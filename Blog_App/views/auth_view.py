from django.shortcuts import render

def login_page(request):
    return render(request, 'auth/login_page.html')

def register_page(request):
    return render(request, 'auth/register_page.html')