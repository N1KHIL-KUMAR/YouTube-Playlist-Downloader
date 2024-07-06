#!/usr/bin/python3

from pytube import Playlist
import pyfiglet
import time
a_bSa = '\x1b[1;32m'
#created by nikhil kumar
#https://x.com/NIKHIL_KUM4R
ab = pyfiglet.figlet_format('Downloader')
print(a_bSa + ab)
time.sleep(2)
def download_playlist_videos(playlist_url, resolution):

    resolution_dict = {
        "highest": "2160p",
        "high": "1440p",
        "medium": "1080p",
        "low": "720p",
        "very low": "360p"
    }

    if resolution in resolution_dict:
        print("\t")
        print(f"Your Resolution: {resolution}")
        print("\t")
        playlist = Playlist(playlist_url)
        
        for video in playlist.videos:
            # Get the stream with the desired resolution
            stream = video.streams.filter(res=resolution_dict[resolution]).first()
            
            # If the desired resolution stream is not available, get the highest resolution available
            if not stream:
                stream = video.streams.get_highest_resolution()
            
            # Download the selected stream
            stream.download()
        
        print("All videos have been downloaded.")
    else:
        print("\t")
        print("\t")
        print("Error: Check your resolution. Available options are 'highest', 'high', 'medium', 'low', and 'very low'.")

if __name__ == "__main__":
    playlist_url = input("Enter your playlist link:- ")
    print("\t")
    print("\t")
    resolution = input("Enter your resolution (highest, high, medium, low, very low):- ").lower()
    download_playlist_videos(playlist_url, resolution)
    





