import json
import requests

from listen_local.integrations import spotify_oauth

ME_URL = 'https://api.spotify.com/v1/me'


def get_current_user(access_token):
    headers = spotify_oauth.get_user_headers_with_token(access_token)
    response = requests.get(
        ME_URL,
        headers=headers
    )
    return json.loads(response.content)
