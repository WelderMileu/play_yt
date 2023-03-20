#!/usr/bin/env python3
from pytube import Search as ssh
from sys import exit, argv as a
from wget import download as dw
from datetime import datetime
from termcolor import colored
from os import system, remove, path

if len(a) < 2:
    print(f'[!] Usage: {a[0]} <search>')
    exit(-1)

s = ssh(a[1])
r = s.results

def dl(a, v_n):
    stream = r[a].vid_info['streamingData']['formats']
    for x in stream:
        if x['quality'] == 'medium':
            u = x['url']
            dw(u, v_n)

def f_d(a): return a.strftime("%d %b %Y")

for x in r:
    author    = x.author
    index     = r.index(x)
    content   = x.title
    publish_d = f_d(x.publish_date)

    today = f_d(datetime.now())
    ms_d  = publish_d == today and colored("TODAY", "blue") or publish_d
    out   = f'[{index}] ({author}) {content} [{ms_d}]'
    print(out)

c = int(input('[?] Instert to ID: '))
if c != ' ':
    v_n = 'video.mp4'
    print('[+] Download your video ...')
    dl(c, v_n)

    if path.exists(v_n):
        print('[+] Play ...')
        system(f'parole {v_n}')
        remove(v_n)
