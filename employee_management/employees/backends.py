from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()


class EmailBackend(ModelBackend):
    """
    Authenticate using EMAIL or USERNAME (stable & safe)
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        if not username or not password:
            return None

        # 1️⃣ Try email login (loop through all users with same email)
        users = User.objects.filter(email=username, is_active=True)

        for user in users:
            if user.check_password(password):
                return user

        # 2️⃣ Fallback: username login
        try:
            user = User.objects.get(username=username, is_active=True)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

        return None
