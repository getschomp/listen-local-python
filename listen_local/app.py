import json
import os
import requests
import urllib

from flask import flash, Flask, render_template, redirect, url_for, request, session

from listen_local.models import spotify_oauth
from listen_local.models import spotify_user
from listen_local.models import events

app = Flask(__name__, static_url_path='/listen_local/static')
app.secret_key = os.environ.get('SECRET_KEY')

@app.route("/")
def index():
    user_response = spotify_user.get_current_user(session.get('access_token'))
    error = user_response.get('error')
    if error:
        flash(error['message'])
    return render_template(
        'index.html',
        user=user_response,
    )


@app.route("/spotify_auth", methods=['POST'])
def spotify_auth():
    params = urllib.parse.urlencode({
        'client_id': os.environ.get('SPOTIFY_CLIENT_ID'),
        "response_type": "code",
        'scopes': 'playlist-modify-private user-read-email',
        'redirect_uri': url_for('set_session', _external=True)
    })
    spotify_auth_url = "https://accounts.spotify.com/authorize?%s" % params
    return redirect(spotify_auth_url)


@app.route("/playlist_create", methods=['POST'])
def playlist_create():
    try:
        concerts = events.get_local_concerts(
            request.form.get('city'),
            request.form.get('state'),
            request.form.get('start_date'),
            request.form.get('end_date')
        ).content
        # TODO: Create Playlist, Add Songs based on artists
        flash('Playlist Successfully Created')
    except:
        flash('Problem with playlist creation :(')
    return redirect(url_for('index'))


@app.route("/set_session")
def set_session():
    code = request.args['code']
    code_payload = spotify_oauth.get_code_payload(code)
    post_request = requests.post(
        "https://accounts.spotify.com/api/token",
        data=code_payload,
        headers=spotify_oauth.get_basic_auth_header()
    )
    response_data = json.loads(post_request.text)
    access_token = response_data["access_token"]
    # TODO: Handle expiration and refreshing
    # response_data["refresh_token"], response_data["token_type"], response_data["expires_in"]
    session['access_token'] = response_data["access_token"]
    return redirect(url_for('index'))
