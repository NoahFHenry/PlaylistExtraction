import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint

client_credentials_manager = SpotifyClientCredentials(client_id = "c66823cbec64401293a66054c2fbce21", client_secret = "6aa3961e24654e51a966f0b4800f60c9")
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

# paste link here: https://open.spotify.com/playlist/69N5GrdsCrd9l7iqpcoLc7?si=5b398ccd993547a9

pl_id = 'spotify:playlist:2cRhVlh3JXpGnhYH3cHIlr'
offset = 0

while True:
    response = sp.playlist_items(pl_id,
                                 offset=offset,
                                 fields='items.track.id,total',
                                 additional_types=['track'])
    
    if len(response['items']) == 0:
        break
    
    pprint(response['items'])
    offset = offset + len(response['items'])
    print(offset, "/", response['total'])
