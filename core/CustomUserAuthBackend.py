from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import authentication
from rest_framework import exceptions

class EmailOrUsernameModelBackend(authentication.BaseAuthentication):
    """
    This is a ModelBacked that allows authentication with either a username or an email address.

    """
    def authenticate(self, request):
        username = request.META.get('HTTP_X_USERNAME')
        if '@' in username:
            kwargs = {'email': username}
        else:
            kwargs = {'username': username}
        try:
            user = get_user_model().objects.get(**kwargs)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

    def get_user(self, username):
        try:
            return get_user_model().objects.get(pk=username)
        except get_user_model().DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')