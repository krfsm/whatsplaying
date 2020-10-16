import json
import spotipy
import spotipy.oauth2 as oauth2
import sys
import time

from obswebsocket import obsws, requests

scope = 'user-read-private user-read-currently-playing'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

playing_now = ""
client = obsws("localhost", 4444, "ThisIsVerySecret")

while True:
    sp_oauth = spotipy.SpotifyOAuth(scope=scope,username=username)

    if sp_oauth:
        sp = spotipy.Spotify(oauth_manager=sp_oauth)
        client.connect()
        for i in range (0, 359):
            results = sp.currently_playing()
            if results == None or results['item'] == None or results['is_playing'] == False:
                if playing_now != "":
                    playing_now = ""
                    client.call(requests.SetTextGDIPlusProperties('WhatsPlaying', text=playing_now))
                    print("Paused or nothing's playing on Spotify.", flush=True)
            else:
                artists = []
                for artist in results['item']['artists']:
                    artists.append(artist['name'])
                title = str(results['item']['name'])
                artist_list = ", ".join(artists)
                playing = artist_list + " - " + title
                print(playing, flush=True)
                if playing_now != playing:
                    playing_now = playing
                    client.call(requests.SetTextGDIPlusProperties('WhatsPlaying', text=playing))
            time.sleep(5)
    else:
        print("Can't get token for ", username)