import sys
import spotipy
import spotipy.util as util
import json

scope = 'user-read-private user-read-currently-playing'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.currently_playing()
    if results == 'None':
        print("")
        sys.exit()
    else:
        print(json.dumps(results,indent=2,sort_keys=True))
        
        for item in results['item']:
            print(item['artists'][0]['name'] + ' - ' + item['name'])
else:
    print("Can't get token for ", username)