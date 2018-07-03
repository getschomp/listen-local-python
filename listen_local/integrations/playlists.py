import requests
from requests_oauthlib import OAuth1


PLAYLISTS_CREATE_URI = 'https://api.spotify.com/v1/users/{user_id}/playlists'.format


def create_playlist(user_id, city, start_date, end_date):
    OAuth1(
        'YOUR_APP_KEY',
        'YOUR_APP_SECRET',
        'USER_OAUTH_TOKEN',
        'USER_OAUTH_TOKEN_SECRET'
    )
    requests.get(
        PLAYLISTS_CREATE_URI(user_id=user_id),
        payload=_create_playlist_payload(city, start_date, end_date)
    )


def _create_playlist_payload(city, start_date, end_date):
    return {
        "name": f'{City} playing {start_date} {end_date}',
        "description": (
            f'This is whats playing live in your city between '
            f'{start_date} {end_date}'
        )
        "public": false
    }
