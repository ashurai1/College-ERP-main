import os
import django
import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "college_management_system.settings")
django.setup()

from main_app.models import CustomUser, Student, Course, Session

def create_demo_student():
    try:
        # 1. Create a Session
        start_date = datetime.date(2023, 1, 1)
        end_date = datetime.date(2024, 1, 1)
        session, created = Session.objects.get_or_create(
            start_year=start_date,
            end_year=end_date
        )
        if created:
            print(f"Created Session: {session}")
        else:
            print(f"Using existing Session: {session}")

        # 2. Create a Course
        course, created = Course.objects.get_or_create(name="Computer Science")
        if created:
            print(f"Created Course: {course}")
        else:
            print(f"Using existing Course: {course}")

        # 3. Create Student User
        email = "student@student.com"
        password = "student123"
        
        if CustomUser.objects.filter(email=email).exists():
            print(f"User {email} already exists. Resetting password.")
            user = CustomUser.objects.get(email=email)
            user.set_password(password)
            user.save()
        else:
            user = CustomUser.objects.create_user(
                email=email,
                password=password,
                user_type='3',
                first_name="Demo",
                last_name="Student",
                gender="M",
                address="123 Student Way"
            )
            print(f"Created User: {user.email}")

        # 4. Link User to Student Profile
        # Note: The Student model has a OneToOneField to CustomUser.
        # The signal `create_user_profile` in models.py automatically creates a Student instance 
        # when a CustomUser of type 3 is created.
        
        try:
            student = Student.objects.get(admin=user)
        except Student.DoesNotExist:
            print("Signal failed to create Student profile. Creating manually.")
            student = Student.objects.create(admin=user)
        
        student.course = course
        student.session = session
        student.save()
        print(f"Updated Student profile with Course and Session.")
        print("\n--- Demo Student Credentials ---")
        print(f"Email: {email}")
        print(f"Password: {password}")

    except Exception as e:
        print(f"Error creating demo student: {e}")

if __name__ == "__main__":
    create_demo_student()
