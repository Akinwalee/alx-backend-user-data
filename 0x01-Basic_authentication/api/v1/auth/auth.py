#!/usr/bin/env python3
"""
Authentication Template
"""
from flask import request


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
        return False

    def authorization_header(self, request=None) -> str:
        """
        Get the authorization header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Get the current user from request
        """
        return None
