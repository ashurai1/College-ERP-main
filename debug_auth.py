import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "college_management_system.settings")
django.setup()

from django.contrib.auth import authenticate
from main_app.models import CustomUser
from main_app.EmailBackend import EmailBackend

email = 'admin@admin.com'
password = 'admin123'

try:
    user = CustomUser.objects.get(email=email)
    print(f"User found: {user.email}")
    print(f"User type: {user.user_type}")
    print(f"Password in DB (hash): {user.password}")
    
    # Check manually
    if user.check_password(password):
        print("Manual check_password: SUCCEEDED")
    else:
        print("Manual check_password: FAILED")
        
    # Check via Backend
    backend = EmailBackend()
    auth_user = backend.authenticate(username=email, password=password)
    if auth_user:
        print("Backend authenticate: SUCCEEDED")
    else:
        print("Backend authenticate: FAILED")

except CustomUser.DoesNotExist:
    print("User does not exist")
