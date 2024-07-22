from spotipy.oauth2 import SpotifyClientCredentials
from yt_dlp import YoutubeDL
from youtubesearchpython import VideosSearch
import json
import spotipy
import os
import sys

# Welcome message
print("Welcome to GitPlaylist!")

sys.stdout.reconfigure(encoding='utf-8')

# Open the config.json to read the contents
with open('config.json', 'r', encoding='utf-8') as file:
    config = json.load(file)

# Path to folder song output
song_output = 'song_output'

# Path to ffmpeg and ffprobe
ffmpeg_location = 'ffmpeg-master/bin/'

# Fetching the playlist id
playlist_id = config['playlist_id']

# Spotify API credentials
client_id = config['client_id']
client_secret = config['client_secret']

def main():
    # Authenticate using the Client Credentials Flow
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
    print("Spotify Authentication Passed.")

    results = sp.playlist_tracks(playlist_id)

    with open("playlist_info.txt", "w", encoding='utf-8') as txt_file:
        while results:
            for item in results['items']:
                track = item['track']
                song = track['name']
                artist = track['artists'][0]['name']
                print(song, "-", artist)
                track_info = f"{track['name']} - {artist}\n"
                txt_file.write(track_info)
            if results['next']:
                results = sp.next(results)
            else:
                results = None
                print("Finished. Writing to: playlist_info.txt")

    with open('playlist_info.txt', 'r', encoding='utf-8') as track_info:
        # Read each line from the file
        for songquery in track_info:
            songquery = songquery.strip()  # Remove any leading/trailing whitespace
            if not songquery:
                continue  # Skip empty lines

            songquery = track_info.readline()

            songsearch = VideosSearch(songquery, limit=1)

            search_results = songsearch.result()
            video_links = [result['link'] for result in search_results['result']]

            # Print the video links
            for link in video_links:
                print("Downloading video from:", link)

                # Set up yt_dlp options
                ydl_opts = {
                    'format': 'mp3/bestaudio/best',  # Download the best available quality
                    'outtmpl': os.path.join(song_output, '%(title)s.%(ext)s'),  # Save the file with the video title as the name
                    'quiet': False,  # Display progress information
                    'ffmpeg_location': ffmpeg_location,  # Path to ffmpeg and ffprobe
                    'postprocessors': [{  # Extract audio using ffmpeg
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                    }]
                }

                try:
                    with YoutubeDL(ydl_opts) as ydl:
                        # Download the video and extract information
                        info_dict = ydl.extract_info(link, download=True)
                        audio_title = info_dict.get('title', None)
                        audio_description = info_dict.get('description', None)
                        audio_duration = info_dict.get('duration', None)

                except Exception as e:
                    print(f"An error occurred while downloading {link}: {e}")

if __name__ == "__main__":
    main()
    input()
