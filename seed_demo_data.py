import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_project.settings')
django.setup()

from tasks.models import Task
from datetime import date, timedelta

def seed():
    print("Seeding demo task data...")
    if Task.objects.exists():
        print("Tasks already exist. Skipping seed.")
        return

    sample_tasks = [
        {
            'title': 'Setup MySQL Database & Django Project',
            'description': 'Configure MySQL connection settings in Django settings.py and apply database migrations.',
            'category': 'Work',
            'priority': 'High',
            'status': 'Completed',
            'due_date': date.today(),
        },
        {
            'title': 'Design Responsive Task Dashboard UI',
            'description': 'Create Bootstrap 5 master layout, task cards grid, stats counters, and modal forms.',
            'category': 'Work',
            'priority': 'High',
            'status': 'Completed',
            'due_date': date.today(),
        },
        {
            'title': 'Implement Task Filtering & Search Functionality',
            'description': 'Allow users to filter tasks by category, priority, and status, as well as keyword searching.',
            'category': 'Work',
            'priority': 'Medium',
            'status': 'In Progress',
            'due_date': date.today() + timedelta(days=2),
        },
        {
            'title': 'Prepare Internship Presentation Slides',
            'description': 'Summarize features, database architecture, and usage guide for CodSoft Task 1 submission.',
            'category': 'Study',
            'priority': 'High',
            'status': 'Pending',
            'due_date': date.today() + timedelta(days=5),
        },
        {
            'title': 'Review Python Best Practices & PEP8 Guidelines',
            'description': 'Ensure code readability, modular app architecture, and docstring documentation.',
            'category': 'Personal',
            'priority': 'Low',
            'status': 'Pending',
            'due_date': date.today() + timedelta(days=7),
        },
    ]

    for item in sample_tasks:
        Task.objects.create(**item)

    print(f"[SUCCESS] Created {len(sample_tasks)} initial tasks!")

if __name__ == '__main__':
    seed()
