# requires 'pip install youtube_dl'
# requires 'sudo apt-get install ffmpeg'
# converts video to mp3

import youtube_dl

link = input('Paste link here: ')

ydl_opts = \
{
    'format':'bestaudio/best',
    'postprocessors':
        [{
        'key':'FFmpegExtractAudio',
        'preferredcodec':'mp3',
        'preferredquality':'320',
        }],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])
