import json
import os
import datetime

import requests


CLIENT_ID = os.environ.get('SEATGEEK_CLIENT_ID')
CLIENT_ID = os.environ.get('SEATGEEK_CLIENT_SECRET')

EVENTS_GET_URI = 'https://api.seatgeek.com/2/events'


def get_local_concerts_page(city, state, start_date=None, end_date=None, page_num=None):
    params = _get_local_concert_params(city, state, start_date, end_date)
    response = requests.get(
        EVENTS_GET_URI,
        data={
            'page': page_num,
            **params
        },
    )
    return json.loads(response.content)


def _get_local_concert_params(city, state, start_date, end_date):
    if not start_date:
        start_date = datetime.datetime.now()
    if not end_date:
        end_date = (
            start_date - datetime.timedelta(weeks=2)
        ).strftime('%Y-%m-%d')
    return {
        'client_id': CLIENT_ID,
        'venue.state': state,
        'venue.city': city,
        'datetime_utc.gte': start_date,
        'datetime_utc.lte': end_date,
        'taxonomies.name': 'concert',
    }
