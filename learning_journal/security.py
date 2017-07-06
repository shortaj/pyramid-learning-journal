"""."""
import os
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.security import Everyone, Authenticated, Allow
from passlib.apps import custom_app_context
from pyramid.session import check_csrf_token, SignedCookieSessionFactory

class MyRoot(object):
    """docstring for MyRoot"""
    def __init__(self, request):
        self.request = request

    __acl__ = [
        (Allow, Everyone, 'view'),
        (Allow, Authenticated, 'token'),
    ]


def includeme(config):
    """."""
    auth_token = os.environ.get('AUTH_TOKEN', '')
    auth_policy = AuthTktAuthenticationPolicy(
        secret=auth_token,
        hashalg='sha512'
    )
    config.set_authentication_policy(auth_policy)
    config.set_authorization_policy(ACLAuthorizationPolicy())
    config.set_root_factory(MyRoot)

    session_secret = os.environ.get('SESSION_SECRET', 'seekrit')
    session_factory = SignedCookieSessionFactory(session_secret)
    config.set_session_factory(session_factory)
    config.set_default_csrf_options(require_csrf=True)

def check_credentials(username, password):
    """."""
    stored_username = os.environ.get("AUTH_USERNAME", '')
    stored_password = os.environ.get('AUTH_PASSWORD', '')
    is_authenticated = False
    if stored_username and stored_password:
        if username == stored_username:
            if custom_app_context.verify(password, stored_password):
                is_authenticated = True
    return is_authenticated
