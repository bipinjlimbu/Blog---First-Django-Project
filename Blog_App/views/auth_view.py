from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def register_page(request):
    errors = {}
    if request.method == 'POST':
        username = request.POST.get('username').strip()
        first_name = request.POST.get('first_name').strip()
        last_name = request.POST.get('last_name').strip()
        email = request.POST.get('email').strip()
        password = request.POST.get('password').strip()
        confirm_password = request.POST.get('confirm_password').strip()

        if not username:
            errors['username'] = 'Username is required.'
        elif len(username) < 3:
            errors['username'] = 'Username must be at least 3 characters long.'
        elif len(username) > 30:
            errors['username'] = 'Username cannot exceed 30 characters.'
        elif User.objects.filter(username=username).exists():
            errors['username'] = 'Username is already taken.'

        if not first_name:
            errors['first_name'] = 'First name is required.'
        elif not first_name.isalpha():
            errors['first_name'] = 'First name must contain only letters.'
        elif len(first_name) > 30:
            errors['first_name'] = 'First name cannot exceed 30 characters.'
        
        if not last_name:
            errors['last_name'] = 'Last name is required.'
        elif not last_name.isalpha():
            errors['last_name'] = 'Last name must contain only letters.'
        elif len(last_name) > 30:
            errors['last_name'] = 'Last name cannot exceed 30 characters.'

        if not email:
            errors['email'] = 'Email is required.'
        elif User.objects.filter(email=email).exists():
            errors['email'] = 'Email is already registered.'
        
        if not password:
            errors['password'] = 'Password is required.'
        elif len(password) < 6:
            errors['password'] = 'Password must be at least 6 characters long.'
        
        if not confirm_password:
            errors['confirm_password'] = 'Please confirm your password.'
        elif confirm_password != password:
            errors['confirm_password'] = 'Passwords do not match.'

        if not errors:
            user = User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password
            )
            user.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')
        else:
            return render(request, 'auth/register_page.html', {'errors': errors,'data':request.POST})
        
    else:
        return render(request, 'auth/register_page.html')

def login_page(request):
    errors = {}
    if request.method == 'POST':
        identifier = request.POST.get('username').strip()
        password = request.POST.get('password').strip()

        if not identifier:
            errors['username'] = 'Username or Email is required.'

        if not password:
            errors['password'] = 'Password is required.'
        
        if not errors:
            user = authenticate(request, username=identifier, password=password)
            if user is None:
                try:
                    user_obj = User.objects.get(email=identifier)
                    user = authenticate(request, username=user_obj.username, password=password)
                except User.DoesNotExist:
                    user = None

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                errors['general'] = 'Invalid username/email or password.'
        
    return render(request, 'auth/login_page.html', {'errors': errors, 'data': request.POST})

def logout_view(request):
    logout(request)
    return redirect('login')