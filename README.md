# whatsplaying

A tiny [spotipy](https://github.com/plamere/spotipy) script to pull what's
playing on my spotify currently to a local file or feed it to OBS through
a websocket.

The script needs you to set the `user-read-private user-read-currently-playing`
scope in [the Spotify for Developers](https://developer.spotify.com/) personal
data integration (and probably only really needs `user-read-currently-playing`).

The `whatsplaying.env` file should contain your Spotify Client ID and Secret,
and a callback URI (which can be basically any valid URI, but remember that if
you use one controlled by someone else, they can get your tokens).

The script also prints what's playing in the terminal, so you can see if it
breaks or stops getting data from Spotify.

The two versions of the script are:

* `whatsplaying.py`, which prints it to a file to be read by OBS or other software.
* `obs-whatsplaying.py`, which talks to [OBS Websocket](https://github.com/Palakis/obs-websocket) through [OBS-websocket-py](https://github.com/Elektordi/obs-websocket-py/). Make sure to have a good password on your OBS Websocket server if it's open to connections from anywhere else!

To run the script (using bash, in my case):

* Writing to a file: `source whatsplaying.env && python whatsplaying.py` username`
* Sending data directly to OBS: `source whatsplaying.env && python obs-whatsplaying.py username`

TODO: Looking at adding support for vMix. Making it print() UTF-8 characters
-- it's sending it to OBS and writing it to the file, so why doesn't it work
when I print it?
