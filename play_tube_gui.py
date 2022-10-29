#!/usr/bin/python3
import wget
import sys
import subprocess
import os
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from pytube import YouTube
from pytube.cli import on_progress

def main():
    try:
        root = Tk()
        root.title('DOWNLOAD Of THE VIDEO')
        frm  = ttk.Frame(root, padding=20)
        frm.grid()

        def bar_progress(stream, chunk, bytes_remaining):
            size = stream.filesize
            bytes_download = size - bytes_remaining
            percent_of_completion = bytes_download / size * 100
            p    = 0
            
            frm.update_idletasks()
            pb1['value'] = percent_of_completion

            print("{} {}".format(size, percent_of_completion))
            

        def midia_of_video_download():
            domain_url = str(url_path.get())
            yt_url = YouTube(domain_url, on_progress_callback=bar_progress)\
                    .streams\
                    .filter(progressive=True, file_extension='mp4')\
                    .order_by('resolution')\
                    .desc()\
                    .first()\
                    .download()
            
            os.rename(yt_url, 'video.mp4')

        def open_video():
            command = 'parole video.mp4'
            os.system(command)

            if os.path.exists('video.mp4'):
                os.remove('video.mp4')

        pb1 = Progressbar(
            frm,
            orient="horizontal",
            length=200,
            mode='determinate'
        )

        pb1.grid(column=0, row=4, columnspan=3, pady=20)

        label_url_path = Label(frm, text='INSERT INTO DOMAIN URL', font=('Arial', 10, 'bold'))
        label_url_path.grid(column=0, row=0, columnspan=2)
            
        url_path_var = StringVar()

        url_path = Entry(frm, text='', width=30, textvariable=url_path_var)
        url_path.grid(column=0, row=1, columnspan=2, pady=10)
            
        submit = Button(frm, text='Download', command=midia_of_video_download)
        submit.grid(column=0, row=2, columnspan=1)

        open_v = Button(frm, text='open video', command=open_video)
        open_v.grid(column=1, row=2, columnspan=1, padx=10)

        root.mainloop()
    except Exception as err:
        print(err)

if __name__ == '__main__':
    main()
