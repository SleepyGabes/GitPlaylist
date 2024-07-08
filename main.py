from pytube import YouTube
from pydub import AudioSegment
import os
import time
import json
import tkinter as tk
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

song_url = 'song_input.txt'
song_output = 'song_output'
client_id = config['client_id']
client_secret = config['client_secret']
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
track = sp.track(track_id)

def write_file(file_name, content):
    with open(file_name, 'w') as file:
        file.write(content)
    print(f"Content written to '{file_name}' successfully.")


def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return None



def main():
  return

if __name__ == "__main__":
    main()
