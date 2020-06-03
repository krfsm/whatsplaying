# whatsplaying
A tiny [spotipy](https://github.com/plamere/spotipy) script to pull what's
playing on my spotify currently to a local file.

Needs you to set the `user-read-private user-read-currently-playing` scope
in [the Spotify for Developers](https://developer.spotify.com/) personal data
integration (and probably only really needs `user-read-currently-playing`).

The `whatsplaying.env` file should contain your Spotify Client ID and Secret,
and a callback URI (which can be basically any valid URI, but remember that if
you use one controlled by someone else, they can get your tokens).

Added `obs-whatsplaying.py`, which talks to [OBS
Websocket](https://github.com/Palakis/obs-websocket) through
[OBS-websocket-py](https://github.com/Elektordi/obs-websocket-py/). Make sure
to have a good password on your OBS Websocket server if it's open to connections
from anywhere else!

To run the script (using bash, in my case):
`source whatsplaying.env && python whatsplaying.py username`