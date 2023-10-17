import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Set up your Spotify API credentials
client_id = '1ff1356974cb44f88751836978ebbe5c'
client_secret = 'a9923d2fb773461e9f23da4fe5d66f28'

# Initialize the Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Input the artist name
artist_name = input("Enter the name of the artist: ")

# Search for the artist
results = sp.search(q='artist:' + artist_name, type='artist')
artists = results['artists']['items']

if not artists:
    print("Artist not found.")
else:
    artist = artists[0]
    print("Artist Name:", artist['name'])
    print("Popularity:", artist['popularity'])

    # Get the artist's top tracks
    top_tracks = sp.artist_top_tracks(artist['id'])

    print("\nTop Tracks:")
    for track in top_tracks['tracks']:
        print("Track:", track['name'])
        print("Album:", track['album']['name'])
        print("Popularity:", track['popularity'])
        print("Preview URL:", track['preview_url'])
        print()
