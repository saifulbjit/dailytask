from django.contrib.auth.models import User

def is_superadmin(user: User) -> bool:
    return user.is_superuser