from django.conf import settings
from django.contrib.auth.middleware import get_user
from django.utils.deprecation import MiddlewareMixin
from django.utils.functional import SimpleLazyObject


class AuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        assert hasattr(request, 'session'), (
                                                "The Django authentication middleware requires session middleware "
                                                "to be installed. Edit your MIDDLEWARE%s setting to insert "
                                                "'django.contrib.sessions.middleware.SessionMiddleware' before "
                                                "'django.contrib.auth.middleware.AuthenticationMiddleware'."
                                            ) % ("_CLASSES" if settings.MIDDLEWARE is None else "")
        if request.path.startswith('/admin/'):
            request.user = SimpleLazyObject(lambda: get_user(request))
