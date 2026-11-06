#yt-dlp python
# pip install yt-dlp
# pip install imageio-ffmpeg
import yt_dlp

video_url = "https://youtu.be/lGMsfh8AqmM?si=6j4ppJs1xhIC9AXW"

# Configuration options (mimics command-line flags)

ydl_opts = {

"format": "bestaudio/best",

"postprocessors": [

{

"key": "FFmpegExtractAudio",

"preferredcodec": "mp3",

"preferredquality": "192", # You can change to '320' or '0'

}

],

}

# Use a context manager to handle the download

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])

print("Download complete!")