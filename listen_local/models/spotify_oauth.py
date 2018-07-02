import base64
import os

from flask import url_for


def get_basic_auth_header():
    client_auth = '{}:{}'.format(
        os.environ.get('SPOTIFY_CLIENT_ID'),
        os.environ.get('SPOTIFY_CLIENT_SECRECT')
    ).encode('ascii')
    return {
        "Authorization": "Basic {}".format(
            base64.b64encode(client_auth).decode('ascii')
        )
    }


def get_user_headers_with_token(access_token):
    return {
        'Authorization':  f'Bearer {access_token}',
        'content-type': 'application/json',
    }


def get_code_payload(code):
    return {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": url_for('set_session', _external=True)
    }
