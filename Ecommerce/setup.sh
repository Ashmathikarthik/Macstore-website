#!/bin/bash

echo "🚀 Setting up MACESSENTIALSTORE E-commerce Project..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✅ Python3 found: $(python3 --version)"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install requirements
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Run migrations
echo "🗄️ Running database migrations..."
python manage.py makemigrations
python manage.py migrate

# Create static files directory if it doesn't exist
if [ ! -d "EcomApp/static" ]; then
    echo "📁 Creating static files directory..."
    mkdir -p EcomApp/static/images
    mkdir -p EcomApp/static/css
    mkdir -p EcomApp/static/js
fi

echo "✅ Setup complete!"
echo ""
echo "🎉 To start the server, run:"
echo "   source venv/bin/activate"
echo "   python manage.py runserver"
echo ""
echo "🌐 Then visit: http://127.0.0.1:8000"
echo ""
echo "📱 Features available:"
echo "   - Homepage with product showcase"
echo "   - Enhanced cart with dynamic offers"
echo "   - Comprehensive support page"
echo "   - Product pages with categories"
echo "   - Login/Register functionality" 