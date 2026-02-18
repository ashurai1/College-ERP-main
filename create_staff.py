import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "college_management_system.settings")
django.setup()

from main_app.models import CustomUser, Staff, Course

def create_demo_staff():
    try:
        # 1. Ensure Course exists
        course, created = Course.objects.get_or_create(name="Computer Science")
        if created:
            print(f"Created Course: {course}")
        else:
            print(f"Using existing Course: {course}")

        # 2. Create Staff User
        email = "staff@staff.com"
        password = "staff123"
        
        if CustomUser.objects.filter(email=email).exists():
            print(f"User {email} already exists. Resetting password.")
            user = CustomUser.objects.get(email=email)
            user.set_password(password)
            user.save()
        else:
            user = CustomUser.objects.create_user(
                email=email,
                password=password,
                user_type='2',
                first_name="Demo",
                last_name="Staff",
                gender="F",
                address="456 Staff Lane"
            )
            print(f"Created User: {user.email}")

        # 3. Link User to Staff Profile
        try:
            staff = Staff.objects.get(admin=user)
        except Staff.DoesNotExist:
            print("Signal failed to create Staff profile. Creating manually.")
            staff = Staff.objects.create(admin=user)
        
        staff.course = course
        staff.save()
        print(f"Updated Staff profile with Course.")
        print("\n--- Demo Staff Credentials ---")
        print(f"Email: {email}")
        print(f"Password: {password}")

    except Exception as e:
        print(f"Error creating demo staff: {e}")

if __name__ == "__main__":
    create_demo_staff()
