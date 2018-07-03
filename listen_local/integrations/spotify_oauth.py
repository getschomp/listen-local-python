import base64
import os
import json
import urllib

import requests

from flask import url_for


def get_login_url():
    return 'https://accounts.spotify.com/authorize?%s' % _get_login_params()


def request_tokens(code):
    post_request = requests.post(
        "https://accounts.spotify.com/api/token",
        data=_get_code_payload(code),
        headers=_get_basic_auth_header()
    )
    return json.loads(post_request.text)


def get_user_headers_with_token(access_token):
    return {
        'Authorization':  f'Bearer {access_token}',
        'content-type': 'application/json',
    }


def _get_basic_auth_header():
    client_auth = '{}:{}'.format(
        os.environ.get('SPOTIFY_CLIENT_ID'),
        os.environ.get('SPOTIFY_CLIENT_SECRECT')
    ).encode('ascii')
    return {
        "Authorization": "Basic {}".format(
            base64.b64encode(client_auth).decode('ascii')
        )
    }


def _get_login_params():
    return urllib.parse.urlencode({
        'client_id': os.environ.get('SPOTIFY_CLIENT_ID'),
        "response_type": "code",
        'scopes': 'playlist-modify-private user-read-email',
        'redirect_uri': url_for('set_session', _external=True)
    })


def _get_code_payload(code):
    return {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": url_for('set_session', _external=True)
    }
