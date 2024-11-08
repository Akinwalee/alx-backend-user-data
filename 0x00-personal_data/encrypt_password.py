#!/usr/bin/env python3
"""
Encrypt passwords
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hassh password
    """
    hashed = bcrypt.hashpw(password.encode(utf-8), bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Check if a hashed password corresponds to a given password
    """
    validity = bcrypt.checkpw(password.encode("utf-8"), hashed_password)
    return validity
