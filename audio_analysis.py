from auth import sp
from fetch_history import fetch_recent_tracks

def get_audio_features():
  # fetch recent tracks
  results = sp.current_user_recently_played(limit=10)
  track_features = []

  for item in results['items']:
    track = item['track']
    track_id = track['id']
    track_name = track['name']
    track_artists = track['artists'][0]['name']
  
  # fetch audio features for the track
  audio_features = sp.audio_features([track_id])

  # Extract all relevant audio features
  features = {
    'track': track_name, 
    'artist': artist_name,
    'danceability': audio_features['danceability'],
    'energy': audio_features['energy'],
    'valence': audio_features['valence'],
    'tempo': audio_features['tempo'],

    
  }
  track_features.append(features)
  # Print extracted features
  for idx, track in enumerate(track_features):
      print(f"{idx+1}. {track['track']} by {track['artist']}")
      print(f"   🎵 Danceability: {track['aanceability']}")
      print(f"   🔥 Energy: {track['energy']}")
      print(f"   😊 Valence: {track['valence']}")
      print(f"   🕒 Tempo: {track['tempo']} BPM\n")

  return track_features


# Run function to get audio features
if __name__ == "__main__":
    get_audio_features()
