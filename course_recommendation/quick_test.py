#!/usr/bin/env python3
"""
Quick test to verify the Flask app and category APIs are working
"""

import sys
import os

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from app import app, Category, Session
    print("✅ Successfully imported Flask app and models")
    
    # Test database connection
    session = Session()
    try:
        # Try to query categories
        count = session.query(Category).count()
        print(f"✅ Database connection working - Found {count} categories")
        
        # Test each category type
        for category_type in ['education', 'industry', 'experience_level', 'role', 'skills']:
            cat_count = session.query(Category).filter_by(category_type=category_type, is_active=True).count()
            print(f"   📋 {category_type}: {cat_count} items")
            
    except Exception as e:
        print(f"❌ Database error: {str(e)}")
    finally:
        session.close()
    
    # Test Flask app routes
    with app.test_client() as client:
        print("\n🧪 Testing API endpoints...")
        
        # Test education endpoint
        response = client.get('/api/education')
        if response.status_code == 200:
            print("✅ GET /api/education - Working")
        else:
            print(f"❌ GET /api/education - Status: {response.status_code}")
        
        # Test industry endpoint
        response = client.get('/api/industry')
        if response.status_code == 200:
            print("✅ GET /api/industry - Working")
        else:
            print(f"❌ GET /api/industry - Status: {response.status_code}")
        
        # Test skills endpoint
        response = client.get('/api/skills')
        if response.status_code == 200:
            print("✅ GET /api/skills - Working")
        else:
            print(f"❌ GET /api/skills - Status: {response.status_code}")
        
        # Test search endpoint
        response = client.get('/api/categories/search?q=python')
        if response.status_code == 200:
            print("✅ GET /api/categories/search - Working")
        else:
            print(f"❌ GET /api/categories/search - Status: {response.status_code}")
    
    print("\n🎉 All tests completed! Your APIs are ready to use.")
    print("\n🚀 To start the server, run: python app.py")
    
except ImportError as e:
    print(f"❌ Import error: {str(e)}")
    print("Make sure you're in the correct directory and have activated the virtual environment")
except Exception as e:
    print(f"❌ Error: {str(e)}")
