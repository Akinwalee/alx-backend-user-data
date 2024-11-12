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

        path_alt = path if path.endswith("/") else path + "/"
        if path_alt not in excluded_paths:
            return True

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
