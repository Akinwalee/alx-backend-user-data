#!/usr/bin/env python3
"""
Basic Auth Implementation
"""
from base64 import b64decode
from api.v1.auth.auth import Auth
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """
    Basic Auth
    """
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        Extract base64 from header
        """
        header = authorization_header
        if not header or not isinstance(header, str) or not header.startswith(
                "Basic "):
            return None

        return header.split()[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        Decode Base64
        """
        header = base64_authorization_header
        if not header or not isinstance(header, str):
            return None

        try:
            return b64decode(header).decode("utf-8")
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> str:
        """
        Extract user credentials
        """
        details = decoded_base64_authorization_header
        if not details or not isinstance(details, str) or ":" not in details:
            return (None, None)

        uname, pwd = details.split(":", 1)
        return (uname, pwd)

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar("User"):
        """
        Get the user object from credentials
        """
        if not user_email or not isinstance(user_email, str):
            return None
        if not user_pwd or not isinstance(user_pwd, str):
            return None

        users = User.search({"email": user_email})

        if not users:
            return None

        user = users[0]

        if not user.is_valid_password(user_pwd):
            return None

        return user
