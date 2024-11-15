#!/usr/bin/python3
""" Check response
"""

if __name__ == "__main__":
    from api.v1.auth.basic_auth import BasicAuth
    from api.v1.app import auth

    if auth is None:
        print("'auth' doesn't exist in api/v1/app.py")
        exit(1)

    if not isinstance(auth, BasicAuth):
        print("auth is not an instance of BasicAuth")
        exit(1)

    print("OK", end="")
