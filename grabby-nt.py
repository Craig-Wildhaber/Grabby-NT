import os
import sys
from pytube import YouTube

print("Grabby-NT v1.1\n")

DRIVE = os.environ['HOMEDRIVE']
PATH = os.environ['HOMEPATH']
HOME = f"{DRIVE}{PATH}"
PARAMS = len(sys.argv)
SWITCH = sys.argv[1]

def get_media(dir, type, logic_counter):

    link = sys.argv[logic_counter]
    yt = YouTube(link)
    print(f"Requested media: {yt.title}")
    newfile = input("Enter filename: ")
    selected_media = ''

    if type == "-v":

        selected_media = yt.streams.get_highest_resolution()
        directory = f"{dir}\Videos\\"
    
    elif type == "-a":

        selected_media = yt.streams.get_audio_only()
        directory = f"{dir}\Music\\"


    else:
        print("Usage: ytget <options> <video-link>")
        print("-a: Audio only download \n-v: Full A/V download")

    print(f"Downloading to: {directory}")
    selected_media.download(output_path=f"{directory}", filename=f"{newfile}.mp4")
    print("Download complete.")

counter = 2

while counter != PARAMS:

    if PARAMS > 1:
        get_media(HOME, SWITCH, counter)
    
    counter += 1
