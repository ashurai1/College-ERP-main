import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "college_management_system.settings")
django.setup()

from main_app.models import CustomUser

try:
    user = CustomUser.objects.get(email='admin@admin.com')
    user.set_password('admin123')
    user.save()
    print("Password reset successfully using set_password().")
except CustomUser.DoesNotExist:
    print("User not found.")
