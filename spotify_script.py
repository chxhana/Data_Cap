import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

#spotify API credentials
client_id = 'f2f940cfa8454d4f9df2b0127edbb5bc'
client_secret = '9bf7b2df3dce48c6996867215e807fd8'
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

 #2013 to 2023 years
years = list(range(2013, 2024)) 

#track IDs
all_track_ids = []

for year in years:
    #search for playlists representing the top tracks for the current year
    search_query = f'Top Hits {year}'  
    limit_per_search = 1  #one playlist per year

    results = sp.search(q=search_query, type='playlist', limit=limit_per_search)
    
    #check if playlists were found
    if 'playlists' in results and 'items' in results['playlists']:
        playlists = results['playlists']['items']
        for playlist in playlists:
            #get the tracks from the playlist
            playlist_id = playlist['id']
            playlist_tracks = sp.playlist_tracks(playlist_id)
            
            #extract track IDs
            track_ids = [track['track']['id'] for track in playlist_tracks['items']]
            
            #append track IDs to the overall list
            all_track_ids.extend(track_ids)
            
            print(f'Total top songs for {year}: {len(all_track_ids)}')

print(f'Total top songs from 2013 to 2023 retrieved: {len(all_track_ids)}')
print(all_track_ids)
