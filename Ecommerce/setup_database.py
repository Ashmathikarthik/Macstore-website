#!/usr/bin/env python
"""
Database setup script for MACESSENTIALSTORE
This script helps set up the database with migrations and creates a superuser.
"""

import os
import sys
import django

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ecommerce.settings')
django.setup()

from django.core.management import execute_from_command_line
from django.contrib.auth import get_user_model

User = get_user_model()

def main():
    print("🚀 Setting up MACESSENTIALSTORE Database...")
    
    try:
        # Make migrations
        print("📝 Creating database migrations...")
        execute_from_command_line(['manage.py', 'makemigrations'])
        
        # Migrate
        print("🔄 Applying migrations...")
        execute_from_command_line(['manage.py', 'migrate'])
        
        # Create superuser if it doesn't exist
        if not User.objects.filter(is_superuser=True).exists():
            print("👤 Creating superuser...")
            print("Please enter the following details for the superuser:")
            
            email = input("Email: ")
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            password = input("Password: ")
            
            if email and password:
                try:
                    user = User.objects.create_superuser(
                        email=email,
                        password=password,
                        first_name=first_name or '',
                        last_name=last_name or ''
                    )
                    print(f"✅ Superuser created successfully: {user.email}")
                except Exception as e:
                    print(f"❌ Error creating superuser: {e}")
            else:
                print("❌ Email and password are required for superuser creation.")
        else:
            print("✅ Superuser already exists.")
        
        print("\n🎉 Database setup completed successfully!")
        print("\n📋 Next steps:")
        print("1. Run: python manage.py runserver")
        print("2. Visit: http://127.0.0.1:8000")
        print("3. Admin panel: http://127.0.0.1:8000/admin")
        
    except Exception as e:
        print(f"❌ Error during setup: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main() 