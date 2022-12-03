#!/usr/bin/python3

import os
import sys
from pytube import YouTube

for arg_num in range(1, len(sys.argv)):

    # Searches for your home directory and saves it as a constant
    HOME = os.environ['HOME']
    # Users downloads directory
    DIRECTORY = f"{HOME}/Downloads"

    # Clears previous command
    os.system("clear")

    # grabs the youtube link from your terminal argument
    link = sys.argv[arg_num]
    # Creates youtube object that represents the online video
    yt = YouTube(link)
    # Displays video title to user
    print(f"{yt.title}\n")

    # Grabs just the audio from the video for faster conversion and download speeds. Strangely it stays in the mp4 format.
    # Which is why you need to convert in the first place. I will find a fix later.
    video = yt.streams.get_audio_only()
    # Downloads the video to your downloads directory
    video.download(output_path=DIRECTORY, filename="video.mp4")
    print("\nDownload Complete\n")

    # Here is where my studies pay off. This section is dependent on the os module, due to the need of shell commands
    # For conversion. This command converts the mp4 file to flac (Free lossless audio codec)
    os.system(f"ffmpeg -i {HOME}/Downloads/video.mp4 {HOME}/Music/video.flac")
    print("\nFile Converted\n")
    # removes old mp4 file from your system so you do not have to.
    os.remove(f"{HOME}/Downloads/video.mp4")
    print("Original File Removed\n")
    # Asks you what you would like to name the converted file.
    filename = input("Enter new filename: ")
    # Changes the file name to your input.
    os.system(f"mv {HOME}/Music/video.flac {HOME}/Music/'{filename}.flac'")
    print("\nComplete\n")
