from pytube import YouTube as yt
from pytube.contrib.search import Search
from spotipy.oauth2 import SpotifyClientCredentials
from yt_dlp import YoutubeDL
from youtubesearchpython import VideosSearch
import json
import spotipy
import os

# Path to folder song output
song_output = 'song_output'

# Path to ffmpeg and ffprobe
ffmpeg_location = 'ffmpeg-master/bin/'

with open('config.json','r') as file:
    config = json.load(file)

# Spotify API credentials
client_id = config['client_id']
client_secret = config['client_secret']

# Authenticate using the Client Credentials Flow
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
print("Spotify Authetication Passed.")

playlist_id = config['playlist_id']

results = sp.playlist_tracks(playlist_id)

with open("playlist_info.txt","w") as txt_file:
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

with open('playlist_info.txt', 'r') as track_info:
    # Read each line from the file
    for songQuery in track_info:
        songQuery = songQuery.strip()  # Remove any leading/trailing whitespace
        if not songQuery:
            continue  # Skip empty lines

        songQuery = track_info.readline()

        songSearch = VideosSearch(songQuery, limit=1)

        search_results = songSearch.result()
        video_links = [result['link'] for result in search_results['result']]

        # Print the video links
        for link in video_links:
            print("Downloading video from:", link)

            # Set up yt_dlp options
            ydl_opts = {
                'format': 'mp3/bestaudio/best',  # Download the best available quality
                'outtmpl': os.path.join(song_output,'%(title)s.%(ext)s'),  # Save the file with the video title as the name
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
