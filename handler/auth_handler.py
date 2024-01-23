from functools import wraps
from flask import request, abort
from typing import Callable

from service.auth_service import user_authentication

def pre_authorize(roles: list()):
    def wrapper(f: Callable):
        @wraps(f)
        def decorator(*args, **kwargs):
            token = None
            if 'Authorization' in request.headers:
                token = request.headers['Authorization']
            if not token or not token.startswith('Bearer '):
                abort(401)
                
            if user_authentication(roles, token):
                return f(*args, **kwargs)
            abort(403)
        return decorator
    return wrapper