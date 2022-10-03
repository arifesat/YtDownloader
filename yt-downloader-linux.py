from __future__ import unicode_literals
import yt_dlp

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '256'
    }],
    'outtmpl': "~/Downloads/Music/%(title)s.%(ext)s" #Music doownload location
    }
ydl_opts_vid = {
    'ignoreerrors' : 'True',
    'format' : 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    'outtmpl': "~/Downloads/Video/%(title)s.%(ext)s" #Video download location
}
def download_video(video):
    video = video
    yd.download([video])
    
while True:
    selection = int(input("Download Audio or Video?\nVideo: 1\nAudio: 2\nQuit: 0\n"))

    if selection == int(1) or selection == int(2):
        video_link = input("Audio/Video Link: ")
        if selection == int(1):
            with yt_dlp.YoutubeDL(ydl_opts_vid) as yd:
                video = video_link
                download_video(video)
        elif selection == int(2):
            with yt_dlp.YoutubeDL(ydl_opts) as yd:
                video = video_link
                yd.download([video])    

    elif selection == int(0):
        break

    else:
        print("Enter a valid option.\n'1' for video, '2' for audio")