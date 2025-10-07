#!/usr/bin/env python3
"""
Sample data insertion script for categories table
Run this script to populate the categories table with sample data
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import Category, Base
import os
from dotenv import load_dotenv

load_dotenv()

# Database connection
connection_string = "postgresql://neondb_owner:Pl8cWUu0iLHn@ep-tiny-haze-a1w7wrrg.ap-southeast-1.aws.neon.tech/figure_circle"
engine = create_engine(connection_string, connect_args={'connect_timeout': 10})
Session = sessionmaker(bind=engine)

# Sample data for each category type
sample_data = {
    'education': [
        {'name': 'Bachelor of Science', 'description': 'Undergraduate degree in science'},
        {'name': 'Bachelor of Arts', 'description': 'Undergraduate degree in arts'},
        {'name': 'Master of Science', 'description': 'Graduate degree in science'},
        {'name': 'Master of Arts', 'description': 'Graduate degree in arts'},
        {'name': 'PhD', 'description': 'Doctor of Philosophy'},
        {'name': 'MBA', 'description': 'Master of Business Administration'},
        {'name': 'B.Tech', 'description': 'Bachelor of Technology'},
        {'name': 'M.Tech', 'description': 'Master of Technology'},
        {'name': 'B.Com', 'description': 'Bachelor of Commerce'},
        {'name': 'M.Com', 'description': 'Master of Commerce'},
    ],
    'industry': [
        {'name': 'Technology', 'description': 'Information technology and software'},
        {'name': 'Healthcare', 'description': 'Medical and healthcare services'},
        {'name': 'Finance', 'description': 'Banking and financial services'},
        {'name': 'Education', 'description': 'Educational institutions and services'},
        {'name': 'Manufacturing', 'description': 'Industrial manufacturing'},
        {'name': 'Retail', 'description': 'Retail and consumer goods'},
        {'name': 'Consulting', 'description': 'Business consulting services'},
        {'name': 'Media & Entertainment', 'description': 'Media and entertainment industry'},
        {'name': 'Real Estate', 'description': 'Real estate and property'},
        {'name': 'Automotive', 'description': 'Automotive industry'},
    ],
    'experience_level': [
        {'name': 'Entry Level', 'description': '0-2 years of experience'},
        {'name': 'Junior', 'description': '2-4 years of experience'},
        {'name': 'Mid Level', 'description': '4-7 years of experience'},
        {'name': 'Senior', 'description': '7-10 years of experience'},
        {'name': 'Lead', 'description': '10-15 years of experience'},
        {'name': 'Principal', 'description': '15+ years of experience'},
        {'name': 'Director', 'description': 'Executive level with team management'},
        {'name': 'VP', 'description': 'Vice President level'},
        {'name': 'C-Level', 'description': 'Chief Executive level'},
        {'name': 'Intern', 'description': 'Internship or trainee level'},
    ],
    'role': [
        {'name': 'Software Engineer', 'description': 'Develops software applications'},
        {'name': 'Data Scientist', 'description': 'Analyzes and interprets complex data'},
        {'name': 'Product Manager', 'description': 'Manages product development'},
        {'name': 'Marketing Manager', 'description': 'Oversees marketing strategies'},
        {'name': 'Sales Representative', 'description': 'Handles sales activities'},
        {'name': 'HR Manager', 'description': 'Manages human resources'},
        {'name': 'Financial Analyst', 'description': 'Analyzes financial data'},
        {'name': 'Project Manager', 'description': 'Manages project execution'},
        {'name': 'Business Analyst', 'description': 'Analyzes business processes'},
        {'name': 'UX Designer', 'description': 'Designs user experiences'},
        {'name': 'DevOps Engineer', 'description': 'Manages development operations'},
        {'name': 'Quality Assurance', 'description': 'Ensures product quality'},
    ],
    'skills': [
        {'name': 'Python', 'description': 'Python programming language'},
        {'name': 'JavaScript', 'description': 'JavaScript programming language'},
        {'name': 'Java', 'description': 'Java programming language'},
        {'name': 'React', 'description': 'React.js framework'},
        {'name': 'Node.js', 'description': 'Node.js runtime environment'},
        {'name': 'SQL', 'description': 'Structured Query Language'},
        {'name': 'Machine Learning', 'description': 'Machine learning techniques'},
        {'name': 'Data Analysis', 'description': 'Data analysis and visualization'},
        {'name': 'Project Management', 'description': 'Project management methodologies'},
        {'name': 'Agile', 'description': 'Agile development methodology'},
        {'name': 'Communication', 'description': 'Effective communication skills'},
        {'name': 'Leadership', 'description': 'Leadership and team management'},
        {'name': 'Problem Solving', 'description': 'Analytical problem solving'},
        {'name': 'Teamwork', 'description': 'Collaborative teamwork skills'},
        {'name': 'Time Management', 'description': 'Time management and organization'},
    ]
}

def insert_sample_data():
    """Insert sample data into the categories table"""
    session = Session()
    
    try:
        # Check if data already exists
        existing_count = session.query(Category).count()
        if existing_count > 0:
            print(f"Categories table already has {existing_count} records.")
            response = input("Do you want to continue and add more data? (y/n): ")
            if response.lower() != 'y':
                print("Operation cancelled.")
                return
        
        total_inserted = 0
        
        for category_type, items in sample_data.items():
            print(f"\nInserting {category_type} categories...")
            
            for item in items:
                # Check if category already exists
                existing = session.query(Category).filter_by(
                    category_type=category_type,
                    name=item['name']
                ).first()
                
                if existing:
                    print(f"  - {item['name']} already exists, skipping...")
                    continue
                
                # Create new category
                new_category = Category(
                    category_type=category_type,
                    name=item['name'],
                    description=item['description'],
                    is_active=True
                )
                
                session.add(new_category)
                print(f"  + Added: {item['name']}")
                total_inserted += 1
        
        # Commit all changes
        session.commit()
        print(f"\n✅ Successfully inserted {total_inserted} new categories!")
        
        # Display summary
        print("\n📊 Summary by category type:")
        for category_type in sample_data.keys():
            count = session.query(Category).filter_by(
                category_type=category_type, 
                is_active=True
            ).count()
            print(f"  - {category_type}: {count} items")
        
    except Exception as e:
        session.rollback()
        print(f"❌ Error inserting data: {str(e)}")
    finally:
        session.close()

def display_categories():
    """Display all categories in the database"""
    session = Session()
    
    try:
        print("\n📋 Current Categories in Database:")
        print("=" * 50)
        
        for category_type in sample_data.keys():
            categories = session.query(Category).filter_by(
                category_type=category_type,
                is_active=True
            ).order_by(Category.name).all()
            
            print(f"\n{category_type.upper().replace('_', ' ')} ({len(categories)} items):")
            print("-" * 30)
            
            for cat in categories:
                print(f"  • {cat.name}")
                if cat.description:
                    print(f"    └─ {cat.description}")
        
    except Exception as e:
        print(f"❌ Error displaying data: {str(e)}")
    finally:
        session.close()

if __name__ == "__main__":
    print("🚀 Categories Data Management")
    print("=" * 40)
    
    while True:
        print("\nOptions:")
        print("1. Insert sample data")
        print("2. Display current categories")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '1':
            insert_sample_data()
        elif choice == '2':
            display_categories()
        elif choice == '3':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")
