# downloads best video + best audio

import youtube_dl

link = input('Paste link here: ')

ydl_opts = \
{
    'format':'bestvideo+bestaudio'
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])
