from auth import sp  # Import authenticated Spotify instance

def fetch_recent_tracks():
    results = sp.current_user_recently_played(limit=10)  # Get last 10 songs

    for idx, item in enumerate(results['items']):
        track = item['track']
        print(f"{idx+1}. {track['name']} - {track['artists'][0]['name']}")

# Run function to fetch recent tracks
fetch_recent_tracks()
