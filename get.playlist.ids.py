# Note. For this, you'll need to install the Spotipy package (https://spotipy.readthedocs.io/en/2.21.0/) and create an app in the Spotify API dashboard (https://developer.spotify.com/dashboard/login), if you don't already have one you can use. Once you've registered and created an app, grab your automatically generated client ID and secret. DO NOT SHARE THESE WITH OTHERS!

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint

client_credentials_manager = SpotifyClientCredentials(client_id = "YOUR_CLIENT_ID", client_secret = "YOUR_CLIENT_SECRET")
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

# example playlist link: https://open.spotify.com/playlist/37i9dQZF1DX4CZc00Cxa3X?si=ec0810ebbad94865
#    playlist ID = string between playlist/ and ? (i.e., 37i9dQZF1DX4CZc00Cxa3X)

pl_id = 'spotify:playlist:PLAYLIST_ID_HERE'
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
