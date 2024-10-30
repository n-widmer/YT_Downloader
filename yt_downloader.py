import yt_dlp
from sys import argv

def download_video(url, output_path='./Pirated_vids'):
    ydl_opts = {
        'outtmpl': f'{output_path}/%(title)s.%(ext)s', 
        'format': 'best', #best quality
    }

    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

video_url = argv[1]

download_video(video_url)

