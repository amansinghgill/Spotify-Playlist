# Billboard Hot 100 Top Songs to Spotify Playlist

This Python script allows you to create a Spotify playlist based on the Billboard Hot 100 chart for a specific date. It uses the Spotify API to search for songs and create a private playlist with the top songs from the specified date. Here's how you can set it up and use it:

## Prerequisites

Before you can run this script, you'll need to set up some prerequisites:

1. **Spotify Developer Account**: You need a Spotify Developer Account to get your API credentials (Client ID and Client Secret). You can create one at the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).

2. **Environment Variables**: Set up environment variables for your Spotify API credentials. You can do this by adding the following lines to your environment variables or by creating a `.env` file in your project directory:

   ```python
   SPOTIFY_CLIENT_ID=your_client_id
   SPOTIFY_CLIENT_SECRET=your_client_secret
   ```

3. **Python Libraries**: Make sure you have the required Python libraries installed. You can install them using `pip`:

   ```bash
   pip install beautifulsoup4 requests spotipy
   ```

## Usage

1. Run the script:

   ```bash
   python main.py
   ```

2. You will be prompted to enter a date in the format `YYYY-MM-DD`. This is the date for which you want to find the top songs on the Billboard Hot 100 chart.

3. The script will then fetch the top songs for the specified date from the Billboard Hot 100 chart.

4. It will authenticate with the Spotify API using your credentials and create a private playlist named `[Date] Billboard 100` on your Spotify account.

5. Finally, it will search for each song on Spotify and add the matching tracks to the newly created playlist.


<div style="text-align:center">
  <img src="https://github.com/amansinghgill/Spotify-Playlist/assets/90486946/88f2557a-6030-4577-a703-eb4832d41d72" alt="example" width="600px" style="display: block; padding-bottom: 20px;">
</div>

<div style="text-align:center">
  <img src="https://github.com/amansinghgill/Spotify-Playlist/assets/90486946/72c8b517-b664-4a37-8c01-84c7d5cdd992" alt="UI" width="600px" style="display: block;">
</div>

## Notes

- If a song is not found on Spotify, it will be skipped, and you will see a message indicating which songs were not found.

- The script uses the Spotify API's `playlist-modify-private` scope to create and modify private playlists on your account.

- The Spotify API requires you to set up a redirect URI when creating your Spotify Developer Application. In the script, it's set to "http://example.com". You can change it to your own redirect URI if needed.

- The script caches the Spotify access token in a file named `token.txt` for future use. Make sure to keep this file secure.

- The Spotify playlist is created as a private playlist by default. You can change the `public` parameter in the `user_playlist_create` function to `True` if you want to make it public.

- Replace `'your_spotify_username'` with your actual Spotify username.

Enjoy creating your personalized Billboard Hot 100 playlists on Spotify!
