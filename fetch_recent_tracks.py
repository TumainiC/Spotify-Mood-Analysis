import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
    scope="user-read-recently-played user-library-read"
))

# Fetch the 10 most recent tracks played
recent_tracks = sp.current_user_recently_played(limit=10)

# Print track details
for idx, item in enumerate(recent_tracks['items']):
    track = item['track']
    print(f"{idx+1}. {track['name']} - {track['artists'][0]['name']} (ID: {track['id']})")

user_profile = sp.current_user()
print(user_profile)

