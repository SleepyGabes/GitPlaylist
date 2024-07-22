from spotipy.oauth2 import SpotifyClientCredentials
from yt_dlp import YoutubeDL
from youtubesearchpython import VideosSearch
import tkinter as tk
import subprocess
import json
import spotipy
import os
import sys

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

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("GitPlaylist")

        self.label = tk.Label(self.root, text="Welcome to GitPlaylist", font=('Arial', 20))
        self.label.pack(padx=5, pady=5)

        self.config = tk.Button(self.root, text="Open config.json", font=('Arial', 14), command=self.open_config)
        self.config.pack(padx=10, pady=10)

        self.start = tk.Button(self.root, text="Start", font=('Arial', 14), command=self.start_process)
        self.start.pack(padx=10, pady=10)

        self.start = tk.Button(self.root, text="Close", font=('Arial', 14), command=self.close)
        self.start.pack(padx=10, pady=10)

    def open_config(self):
        subprocess.Popen(r'notepad config.json')

    def start_process(self):
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

    def close(self):
        exit()

def main():
    root = tk.Tk()
    app = GUI(root)
    root.geometry("300x225")
    root.mainloop()

if __name__ == "__main__":
    main()
    input()
