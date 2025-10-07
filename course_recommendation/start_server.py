#!/usr/bin/env python3
"""
Simple script to start the Flask server with proper configuration
"""

import os
import sys

# Add current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

if __name__ == '__main__':
    try:
        from app import app, socketio
        
        print("🚀 Starting FigureCircle Backend Server...")
        print("=" * 50)
        print("📡 Server will be available at: http://localhost:5000")
        print("🔗 Category APIs available at:")
        print("   • GET /api/education")
        print("   • GET /api/industry") 
        print("   • GET /api/experience-level")
        print("   • GET /api/role")
        print("   • GET /api/skills")
        print("   • GET /api/categories/search?q=python")
        print("=" * 50)
        print("💡 Press Ctrl+C to stop the server")
        print()
        
        # Start the server
        socketio.run(app, debug=True, host='0.0.0.0', port=5000)
        
    except ImportError as e:
        print(f"❌ Import Error: {str(e)}")
        print("Make sure you have activated the virtual environment:")
        print("   source venv/bin/activate")
    except Exception as e:
        print(f"❌ Error starting server: {str(e)}")
        print("Check your database connection and dependencies")
