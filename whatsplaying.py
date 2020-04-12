import sys
import spotipy
import spotipy.util as util
import time

scope = 'user-read-private user-read-currently-playing'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    while True:
        results = sp.currently_playing()
        f = open("playing.txt","w+")
        contents = str(f.read())
        # print(json.dumps(results, indent=2, sort_keys=True))
        if results == 'None':
            if contents != "":
                f.write("")
                f.close()
            else:
                f.close()
        else:
            artists = []
            for artist in results['item']['artists']:
                artists.append(artist['name'])
            title = str(results['item']['name'])
            artist_list = ", ".join(artists)
            playing = artist_list + " - " + title
            if contents != playing:
                f.write(playing)
                f.close()
            else:
                f.close()
        time.sleep(5)
else:
    print("Can't get token for ", username)