from typing import Optional

from django.contrib.auth.models import User


def get_user_by_credentials(username: str, password: str) -> Optional[User]:
    try:
        user = User.objects.get(username=username)
        if not user.check_password(password):
            return None
        return user
    except:
        return None
