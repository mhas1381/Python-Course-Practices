from bs4 import BeautifulSoup
import requests
import spotipy
import os
from dotenv import load_dotenv

load_dotenv()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
}
user_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")

web_page = requests.get(url=f"https://www.billboard.com/charts/hot-100/{user_date}", headers=headers)

soup = BeautifulSoup(web_page.text, 'html.parser')

data = soup.find_all(name='h3', class_='a-truncate-ellipsis')

songs = [song.get_text().strip() for song in data]


CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URL = os.getenv('REDIRECT_URL')

scope = "user-read-currently-playing playlist-read-private playlist-read-collaborative playlist-modify-public playlist-modify-private"

auth_manager = spotipy.oauth2.SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URL,
                                           scope=scope)
sp = spotipy.Spotify(auth_manager=auth_manager)

user_id = sp.current_user()['id']
create_play_list = sp.user_playlist_create(user =user_id ,name =  f"{user_date} nostalgia", public=False, collaborative=False,
                     description='this is a test playlist called by python')

pl = sp.current_user_playlists()['items'][0]

def get_song_id(song_name , track_year ):
    """
    Search for a song by name and return its Spotify track ID.
    """
    query = f"track:{song_name} year: {track_year}"

    # Search Spotify
    results = sp.search(q=query, type='track', limit=1)

    # Check if results exist
    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        track_id = track['id']
        track_name = track['name']
        track_year = track['album']['release_date'].split('-')[0]
        print(f"Song: {track_name} s(Year: {track_year}) - ID: {track_id}")
        return track_id
    else:
        print("No song found!")
        return

songs_id = [song_id for song_id in [get_song_id(song, user_date[:3]) for song in songs] if song_id is not None]


add_to_playlist = sp.playlist_add_items(playlist_id=create_play_list['id'] , items=songs_id , position=None)