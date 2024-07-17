from pytube import YouTube
from pydub import AudioSegment
import os
import time
import json
import tkinter as tk
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

with open('config.json','r') as file:
    config = json.load(file)

# Spotify API credentials
client_id = config['client_id']
client_secret = config['client_secret']

# Authenticate using the Client Credentials Flow
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

playlist_id = config['playlist_id']

results = sp.playlist_tracks(playlist_id)

print("Playlist dump created")
with open("results.json", "w") as dump:
    json.dump(results, dump, indent=4)

while results:
    for item in results['items']:
        track = item['track']
        artist = item['artists']
        print(track['name'], artist['name'])
    if results['next']:
        results = sp.next(results)
    else:
        results = None
