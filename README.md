With pip and python3

Install dependencies

```
source venv/bin/activate
pip install -r requirements.txt
```

Run it
```
FLASK_APP=listen_local/app.py
FLASK_ENV=development
SPOTIFY_CLIENT_ID=<redacted>
SPOTIFY_CLIENT_SECRECT=<redacted>
SEEKGEEK_CLIENT_ID=<redacted>
flask run
```

Navigate to

```
http://localhost:5000/
```
