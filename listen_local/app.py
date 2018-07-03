import json
import os
import requests

from flask import flash, Flask, render_template, redirect, url_for, request, session

from listen_local.integrations import spotify_oauth
from listen_local.integrations import spotify_user
from listen_local.integrations import events

app = Flask(__name__, static_url_path='/listen_local/static')
app.secret_key = os.environ.get('SECRET_KEY')

@app.route("/")
def index():
    user_response = spotify_user.get_current_user(session.get('access_token'))
    error = user_response.get('error')
    if error:
        user_response = None
        flash(error['message'])
    return render_template(
        'index.html',
        user=user_response,
    )


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


@app.route("/spotify_auth", methods=['POST'])
def spotify_auth():
    spotify_login_url = spotify_oauth.get_login_url()
    return redirect(spotify_login_url)


@app.route("/set_session")
def set_session():
    response_data = spotify_oauth.request_tokens(request.args['code'])
    session['access_token'] = response_data["access_token"]
    # TODO: Handle expiration and refreshing
    return redirect(url_for('index'))
