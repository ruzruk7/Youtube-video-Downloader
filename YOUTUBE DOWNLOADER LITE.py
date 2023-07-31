# YOUTUBE DOWNLOADER in higher resolutions
# py -m pip install moviepy
# py -m pip install pytube
import os, pytube, moviepy, moviepy.editor
from pytube.cli import on_progress # enable a progress bar of video download
import slugify
def path_formatter(path):
    splitted_orig = path.split('\\')
    format = '/'.join(splitted_orig)
    formatted = format.strip('\"')
    return formatted

# NOTES from  module documentations and online research

# pytube documentation: https://pytube.io/en/latest/index.html#

# pytube.YouTube(url) gets the video location |  yt variable is required to work with youtube media streams using pytube.
# Youtub supports a streaming technique called Dynamic Adaptive Streaming over HTTP (DASH)
# To download a video in quality higher than 720p you need to download the audio then video codec's then merge them afterwards.
#-> a True progressive stream has both audio and video codec (low quality: yt.streams(progressive=True)), else file will have only audio or video.
# To download good quality videos you will want to yt.streams(adaptive=True) known as DASH streams

#    yt.streams([<Stream: itag="18" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.42001E" acodec="mp4a.40.2" progressive="True" type="video">,
#   <Stream: itag="22" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.64001F" acodec="mp4a.40.2" progressive="True" type="video">,
#   <Stream: itag="137" mime_type="video/mp4" res="1080p" fps="30fps" vcodec="avc1.640028" progressive="False" type="video">,
#   <Stream: itag="250" mime_type="audio/webm" abr="70kbps" acodec="opus" progressive="False" type="audio">,
#   <Stream: itag="251" mime_type="audio/webm" abr="160kbps" acodec="opus" progressive="False" type="audio">])

# need to use FFMPEG for combining the two files 

# video codec avc1 is better than vp9
# .mp4 format is better than .webm


# moviepy documentation: https://zulko.github.io/moviepy/index.html 
# moviepy module allows for video processing 


print('Welcome to Youtube Video Downloader\n\n')
print('***WARNING: Downloading videos for commercial use, uploading as your own video or anything in between is illegal. I will not be held accountable for any illegal activity done with this program. :WARNING***\n\n')
print('NOTE: More powerful CPU\'s will lead to quicker combining times\n')
print('To exit at anytime, Enter: Quit\nNOTE: if an action is being processed it is recommeded to not end the program')
destination_location = input('Please enter the location you want your video/audio files and merged files downloaded to.\nEntered: ')
destination_dir = path_formatter(destination_location)
url = input('\nPlease enter the youtube video\'s URL\nEntered: ')

active = True      
while active:
    print('------------------------------------------------------MAIN MENU------------------------------------------------------')
    mode = input('Download video, Enter: DOWNLOAD\t\tDifferent Youtube video, Enter: URL\t\t To exit, Enter: QUIT\nEntered: ').lower()
    if mode == 'url':
        url = input('\nPlease enter the youtube video\'s URL\nEntered: ')
    if(len(url) > 1):
        yt = pytube.YouTube(url, on_progress_callback=on_progress) # yt variable is required to work with pytube. pytube assumes this variable is in source code 
        # pytube.YouTube()  has an argument use_oauth and allow_oauth_cache flags allow you to authorize pytube to interact with YouTube using your account, and can be used to bypass age restrictions or access private videos and playlists. 
        #-> If allow_oauth_cache is set to True, you should only be prompted to do so once, after which point pytube will cache the tokens it needs to act on your behalf. 
        #-> Otherwise, you will be prompted again for each action that requires you to be authenticated.