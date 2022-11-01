import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint

client_credentials_manager = SpotifyClientCredentials(client_id = "XXX", client_secret = "XXX")
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

pl_id = 'spotify:playlist:XXX'
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
