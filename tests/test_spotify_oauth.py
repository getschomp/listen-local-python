import os

import mock

import listen_local.models.spotify_oauth as module


def test_get_user_header_with_token():
    result = module.get_user_headers_with_token('token')
    assert result == {
        'Authorization':  f'Bearer token',
        'content-type': 'application/json',
    }


@mock.patch.dict(os.environ,{'SPOTIFY_CLIENT_ID': 'client_id'})
@mock.patch.dict(os.environ,{'SPOTIFY_CLIENT_SECRECT': 'client_secret'})
def test_get_basic_auth_header():
    assert module.get_basic_auth_header() == {'Authorization': 'Basic Y2xpZW50X2lkOmNsaWVudF9zZWNyZXQ='}


@mock.patch.object(module, 'url_for', return_value='/redirect')
def test_get_code_payload(code):
    module.get_code_payload('code')
    assert  {
        'grant_type': "authorization_code",
        'code': 'code',
        'redirect_uri': '/redirect'
    }
