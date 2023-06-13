import os
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Environment variables for Spotify API credentials
CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')

# Prompting for a date input in a specific format
target_date = input("Enter the date (YYYY-MM-DD) to find the top songs: ")

# Fetching data from Billboard Hot 100 for the given date
billboard_url = f"https://www.billboard.com/charts/hot-100/{target_date}"
response = requests.get(billboard_url)

# Parsing HTML to extract song titles
soup = BeautifulSoup(response.text, 'html.parser')
song_titles_html = soup.select("li ul li h3")
song_titles = [title.getText().strip() for title in song_titles_html]

# Setting up Spotify API authentication
spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="playlist-modify-private",
    redirect_uri="http://example.com",
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    show_dialog=True,
    cache_path="token.txt",
    username='your_spotify_username'
))

# Fetching the current user's Spotify ID
spotify_user_id = spotify.current_user()["id"]
print(spotify_user_id)

# Searching for songs on Spotify and collecting URIs
song_uris = []
search_year = target_date.split("-")[0]
for song in song_titles:
    search_result = spotify.search(q=f"track:{song} year:{search_year}", type="track")
    print(search_result)
    try:
        song_uri = search_result["tracks"]["items"][0]["uri"]
        song_uris.append(song_uri)
    except IndexError:
        print(f"{song} not found on Spotify. Skipped.")

# Creating a new private playlist on Spotify
new_playlist = spotify.user_playlist_create(user=spotify_user_id, name=f"{target_date} Billboard 100", public=False)
print(new_playlist)

# Adding the collected songs to the new playlist
spotify.playlist_add_items(playlist_id=new_playlist["id"], items=song_uris)