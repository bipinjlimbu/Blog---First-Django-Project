from django.shortcuts import render

def register_page(request):
    errors = {}
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        confirm_password = request.POST.get('confirm_password', '').strip()

        
    return render(request, 'auth/register_page.html')

def login_page(request):
    return render(request, 'auth/login_page.html')
