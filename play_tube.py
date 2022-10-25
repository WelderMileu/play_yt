#!/usr/bin/python3
# 8M@91k5q@K6c
try:
    import cv2
    import sys
    from pytube.cli import on_progress
    from pytube import YouTube
    import os
    import unidecode
    from time import sleep

except Exception as err:
    print(err)

class Simple:
    def __init__(self, domain):
        try:
            self.domain     = str(domain)
            self.video_t    = ''
            self.video_tmp  = 'video.mp4'
            self.video_path = ''

        except Exception as err:
            print(err)

    def download_video(self):
        def execute():
            print("\nDownload video progress ...")
            yt = YouTube(self.domain, on_progress_callback=on_progress)
            download = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

            self.video_t    = yt.title
            self.video_path = download

            os.rename(download, self.video_tmp)

        def reset():
            if os.path.exists(self.video_path):
                os.remove(self.video_path)

            if os.path.exists(self.video_tmp):
                os.remove(self.video_tmp)

        try:
            execute()

        except Exception as err:
            print(err)
            reset()
            execute()

    def remove_video(self):
        if os.path.exists(self.video_tmp):
            os.remove(self.video_tmp)

    def play_video(self):
        try:
            print("\n\nStarting video ...")
            sleep(.5)
            cap = cv2.VideoCapture(self.video_tmp)
            ret, frame = cap.read()

            ts = unidecode.unidecode(self.video_t)

            while (1):
                ret, frame = cap.read()
                cv2.imshow(str(ts), frame)
                cv2.moveWindow(str(ts), 0,0)
                cv2.namedWindow(str(ts))
                cv2.setWindowProperty(str(ts), cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

                if cv2.waitKey(1) & 0xFF == ord('q') or ret==False:
                    cap.release()
                    cv2.destroyAllWindows()
                    break

                cv2.imshow(str(ts), frame)
            
        except Exception as err:
            print(err)

    def main(self):
        Simple.download_video()
        Simple.play_video()
        Simple.remove_video()

if __name__ == '__main__':
    Simple = Simple(sys.argv[1])
    Simple.main()
