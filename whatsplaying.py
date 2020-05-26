import json
import spotipy
import spotipy.util as util
import sys
import time

scope = 'user-read-private user-read-currently-playing'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

while True:
    sp_oauth = spotipy.SpotifyOAuth(scope=scope,username=username)

    if sp_oauth:
        sp = spotipy.Spotify(oauth_manager=sp_oauth)
        for i in range (0, 359):
            results = sp.currently_playing()
            playing_file = open("playing.txt","w+", encoding='utf-8')
            contents = str(playing_file.read())
            if results == None or results['item'] == None:
                if contents != "":
                    playing_file.write("")
                    playing_file.close()
                else:
                    playing_file.close()
            else:
                artists = []
                for artist in results['item']['artists']:
                    artists.append(artist['name'])
                title = str(results['item']['name'])
                artist_list = ", ".join(artists)
                playing = artist_list + " - " + title
                if contents != playing:
                    playing_file.write(playing)
                    playing_file.close()
                else:
                    playing_file.close()
            time.sleep(5)
    else:
        print("Can't get token for ", username)