"""
URL configuration for Ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from EcomApp.views import *
from EcomApp.views import products_page, support_page, contact_page, about_page, contact_form_submit

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('cart/', cart, name='cart'),
]

urlpatterns += [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('forgot-password/', forgot_password_view, name='forgot_password'),
    path('products/', products_page, name='products'),
    path('support/', support_page, name='support'),
    path('contact/', contact_page, name='contact'),
    path('about/', about_page, name='about'),
    path('profile/', profile_view, name='profile'),
    path('contact/submit/', contact_form_submit, name='contact_submit'),
]
