#!/usr/bin/python3
import cv2
import sys
from pytube import YouTube
import os

def download_video(domain):
    try:
        yt = YouTube(str(domain))
        download = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
    
        os.rename(download, 'video.mp4')

    except Exception as err:
        print(err)

def remove_video():
    if os.path.exists('video.mp4'):
        os.remove('video.mp4')

def play_video():
    try:
        cap = cv2.VideoCapture("video.mp4")
        ret, frame = cap.read()

        while (1):
            ret, frame = cap.read()
            cv2.imshow('frame', frame)
            cv2.moveWindow('frame', 40,70)

            if cv2.waitKey(1) & 0xFF == ord('q') or ret==False:
                cap.release()
                cv2.destroyAllWindows()
                break

            cv2.imshow('frame', frame)
            
    except Exception as err:
        print(err)

def main():
    download_video(sys.argv[1])
    play_video()
    remove_video()

if __name__ == '__main__':
    main()
