#!/usr/bin/python3
from pytube import YouTube
from pytube.cli import on_progress
import os
import sys

def main(domain):
    try:
        video_n = 'video.mp4'
        _yt     = YouTube(domain, on_progress_callback=on_progress) \
                .streams \
                .filter(progressive=True, file_extension='mp4') \
                .order_by('resolution') \
                .desc() \
                .first() \
                .download()

        os.rename(_yt, video_n)
        os.system('parole {}'.format(video_n))

        if os.path.exists(video_n):
            os.remove(video_n)

    except Exception as err:
        print(err)

if __name__ == '__main__':
    domain = sys.argv[1]
    main(domain)
