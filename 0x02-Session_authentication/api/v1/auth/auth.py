#!/usr/bin/env python3
"""
Authentication Template
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    Basic Authentication
    """
    def __init__(self):
        """
        Initialization
        """
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determine if auth is required
        """
        if not path or not excluded_paths:
            return True

        for x in excluded_paths:
            if path.startswith(x[:-1]):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Get the authorization header
        """
        if not request or not request.headers.get("Authorization", None):
            return None

        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Get the current user from request
        """
        return None
