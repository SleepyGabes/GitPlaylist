from pytube import YouTube
from pydub import AudioSegment
import os
import time

song_url = 'song_input.txt'
song_output = 'song_output'

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
