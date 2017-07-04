from typing import Optional

from django.contrib.auth.models import User

from jba_core import exceptions


def get_user_by_credentials(username: str, password: str) -> Optional[User]:
    try:
        user = User.objects.get(username=username)
        if not user.check_password(password):
            raise exceptions.IncorrectCredentials
        return user
    except User.DoesNotExist:
        raise exceptions.UserNotFound
    except:
        raise exceptions.SomethingWrong
