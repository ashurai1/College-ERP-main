import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "college_management_system.settings")
django.setup()

from main_app.models import CustomUser

try:
    if not CustomUser.objects.filter(email='admin@admin.com').exists():
        print("Creating superuser...")
        user = CustomUser.objects.create_superuser(
            email='admin@admin.com',
            password='admin123',
            gender='M',
            address='Admin Address',
            user_type='1'
        )
        user.save()
        print('Superuser created successfully.')
    else:
        print('Superuser already exists.')
except Exception as e:
    print(f"Error creating superuser: {e}")
