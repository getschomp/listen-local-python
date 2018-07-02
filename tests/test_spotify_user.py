import mock

import requests

import listen_local.models.spotify_user as module

@mock.patch.object(requests, 'get')
def test_get_current_user(mock_request):
    mock_request.return_value = mock.Mock(content='{"display_name": "allison"}')
    assert module.get_current_user('token') == {"display_name": "allison"}
