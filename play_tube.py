#!/usr/bin/python3
from pytube import YouTube
import sys
import os
from time import sleep

def remove_v():
    video_path = os.listdir()
    
    for x in video_path:
        if x.__contains__(".mp4"):
            os.remove(x)
    
    sleep(.5)

def download_v(share):
    try:
        yt   = YouTube(str(share))
        yt_s = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
        
        sleep(5)
        
        start_video = 'parole --fullscreen "{}"'.format(yt_s)
        os.system(start_video)

    except Exception as err:
        print(err)

def main(share):
    download_v(share)
    remove_v()

if __name__ == '__main__':
    share = sys.argv[1]
    main(share)
