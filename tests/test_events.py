# import os
# import mock
# import pytest
# import events as module

#
# def test_get_local_concert_artists():
#     {
#     "meta":
#         {
#             "total":12,"per_page":10,"page":1
#         },
#     "events":[
#         {
#             "venue":{
#                 "timezone":"America\/New_York",
#             }
#             "performers": [
#                 {
#                     "name": "Fish",
#                     "type": "band",
#                 },
#                 {
#                     "name": "Best Band Name",
#                 }
#             ],
#         }
#     }
#     resulting_artists = get_local_concert_artists(events_response)
#     assert resulting_artists == ['Fish', 'Best Band Name']
