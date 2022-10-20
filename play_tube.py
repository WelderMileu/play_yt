#!/usr/bin/python3
try:
    import cv2
    import sys
    from pytube import YouTube
    import os

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
            yt = YouTube(self.domain)
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
            cap = cv2.VideoCapture(self.video_tmp)
            ret, frame = cap.read()

            ts = self.video_t.encode('utf-8') 

            while (1):
                ret, frame = cap.read()
                cv2.imshow(str(ts), frame)
                cv2.moveWindow(str(ts), 40,70)

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
