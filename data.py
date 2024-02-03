import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Set up Spotify API credentials
client_id = 'f2f940cfa8454d4f9df2b0127edbb5bc'
client_secret = '9bf7b2df3dce48c6996867215e807fd8'
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

search_query = 'Famous hit songs'  # Modify with your desired search query
limit_per_search = 50  # Number of tracks to retrieve per search (max: 50)
total_tracks = 1000  # Total number of tracks to retrieve

# Track IDs
track_ids = []

# Perform multiple search requests to retrieve the desired number of track IDs
offset = 0
while len(track_ids) < total_tracks:
    results = sp.search(q=search_query, type='track', limit=limit_per_search, offset=offset)
    items = results['tracks']['items']
    for item in items:
        track_ids.append(item['id'])
        if len(track_ids) >= total_tracks:
            break
    offset += limit_per_search

print(f'Total track IDs retrieved: {len(track_ids)}')
print(track_ids)

