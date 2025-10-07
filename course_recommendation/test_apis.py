#!/usr/bin/env python3
"""
Test script to verify category APIs are working
"""

import requests
import json

BASE_URL = "http://localhost:5000"

def test_api_endpoint(endpoint, description):
    """Test a single API endpoint"""
    try:
        url = f"{BASE_URL}{endpoint}"
        response = requests.get(url, timeout=10)
        
        print(f"\n🔍 Testing: {description}")
        print(f"📡 URL: {url}")
        print(f"📊 Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            if isinstance(data, dict) and len(data) > 0:
                # Get the first key (like 'education', 'industry', etc.)
                key = list(data.keys())[0]
                count = len(data[key]) if isinstance(data[key], list) else 1
                print(f"✅ Success! Found {count} {key} items")
                return True
            else:
                print(f"⚠️  Success but no data returned")
                return True
        else:
            print(f"❌ Failed with status {response.status_code}")
            try:
                error_data = response.json()
                print(f"   Error: {error_data.get('error', 'Unknown error')}")
            except:
                print(f"   Error: {response.text}")
            return False
            
    except requests.exceptions.ConnectionError:
        print(f"❌ Connection Error: Make sure Flask app is running on {BASE_URL}")
        return False
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

def main():
    """Test all category APIs"""
    print("🚀 Testing Category APIs")
    print("=" * 50)
    
    # Test endpoints
    endpoints = [
        ("/api/education", "Get All Education Categories"),
        ("/api/industry", "Get All Industry Categories"),
        ("/api/experience-level", "Get All Experience Level Categories"),
        ("/api/role", "Get All Role Categories"),
        ("/api/skills", "Get All Skills Categories"),
        ("/api/categories/search?q=python", "Search for 'python'"),
        ("/api/categories/search?q=engineer&type=role", "Search for 'engineer' in roles"),
    ]
    
    results = []
    for endpoint, description in endpoints:
        success = test_api_endpoint(endpoint, description)
        results.append((description, success))
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 TEST SUMMARY")
    print("=" * 50)
    
    passed = sum(1 for _, success in results if success)
    total = len(results)
    
    for description, success in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} - {description}")
    
    print(f"\n🎯 Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! APIs are working correctly.")
    else:
        print("⚠️  Some tests failed. Check the Flask app and database connection.")
    
    print(f"\n💡 Make sure to start your Flask app with: python app.py")

if __name__ == "__main__":
    main()
