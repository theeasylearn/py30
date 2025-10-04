from pytubefix import YouTube
from moviepy import VideoFileClip
import os

# Fixed YouTube video URL
url = "https://www.youtube.com/watch?v=EFsmGhXuSZ4"
mp3_file = "a_output.mp3"

# Create YouTube object
yt = YouTube(url)

# Filter stream for 360p progressive (video + audio)
stream = yt.streams.filter(res="360p", progressive=True).first()

# Output directory (current directory)
output_path = ""

if stream:
    print(f"Downloading '{yt.title}' in 360p to {output_path or 'current directory'} ...")
    downloaded_file = stream.download(output_path=output_path)
    print("Download completed successfully.")
    
    # Convert to MP3 using moviepy
    print('Converting video to MP3...')
    video = VideoFileClip(downloaded_file)
    video.audio.write_audiofile(mp3_file)
    video.close()
    print(f"MP3 saved as '{mp3_file}'")
else:
    print("360p video not available for this video.")