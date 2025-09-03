from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, UserProfile, SupportMessage
from django.db import IntegrityError
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def apple_products(request):
    return render(request, 'apple_products.html')

def cart(request):
    return render(request, 'cart.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if email and password:
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {user.get_full_name() or user.email}!')
                return redirect('home')
            else:
                messages.error(request, 'Invalid email or password. Please try again.')
        else:
            messages.error(request, 'Please fill in all fields.')
    
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        
        if not all([email, password1, password2]):
            messages.error(request, 'Please fill in all required fields.')
            return render(request, 'register.html')
        
        if password1 != password2:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'register.html')
        
        if len(password1) < 8:
            messages.error(request, 'Password must be at least 8 characters long.')
            return render(request, 'register.html')
        
        try:
            user = CustomUser.objects.create_user(
                email=email,
                password=password1,
                first_name=first_name or '',
                last_name=last_name or '',
                phone=phone or ''
            )
            
            # Create user profile
            UserProfile.objects.create(user=user)
            
            # Log the user in
            login(request, user)
            messages.success(request, f'Account created successfully! Welcome, {user.get_full_name() or user.email}!')
            return redirect('home')
            
        except IntegrityError:
            messages.error(request, 'An account with this email already exists.')
        except Exception as e:
            messages.error(request, 'An error occurred. Please try again.')
    
    return render(request, 'register.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')

def forgot_password_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            try:
                user = CustomUser.objects.get(email=email)
                # In a real application, you would send a password reset email here
                messages.success(request, f'If an account with {email} exists, you will receive password reset instructions.')
            except CustomUser.DoesNotExist:
                messages.success(request, f'If an account with {email} exists, you will receive password reset instructions.')
        else:
            messages.error(request, 'Please enter your email address.')
    
    return render(request, 'forgot_password.html')

def products_page(request):
    category = request.GET.get('category', 'all')
    context = {
        'selected_category': category,
        'categories': ['all', 'iphone', 'mac', 'airpods', 'watch']
    }
    return render(request, 'products.html', context)

def support_page(request):
    return render(request, 'support.html')

def contact_page(request):
    return render(request, 'contact.html')

def about_page(request):
    return render(request, 'about.html')

@login_required
def profile_view(request):
    return render(request, 'profile.html')

def contact_form_submit(request):
    if request.method == 'POST':
        try:
            # Get form data
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone', '')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            
            # Validate required fields
            if not all([name, email, subject, message]):
                return JsonResponse({
                    'success': False,
                    'message': 'Please fill in all required fields.'
                })
            
            # Create and save the support message
            support_message = SupportMessage.objects.create(
                name=name,
                email=email,
                phone=phone,
                subject=subject,
                message=message
            )
            
            return JsonResponse({
                'success': True,
                'message': 'Thank you for your message! We will get back to you within 24 hours.'
            })
            
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': 'An error occurred. Please try again.'
            })
    
    return JsonResponse({
        'success': False,
        'message': 'Invalid request method.'
    })
