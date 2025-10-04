from pytubefix import YouTube
import os

# Take YouTube video URL as input
url = input("Enter YouTube video URL:  ")

# Create YouTube object
yt = YouTube(url)

# Filter stream for 720p progressive (video + audio)
stream = yt.streams.filter(res="360p", progressive=True).first()

# Output directory
output_path = r"C:\data\EasyLearn Presentations\cyber security\video"

# Ensure directory exists; if not, create it
os.makedirs(output_path, exist_ok=True)

if stream:
    print(f"Downloading '{yt.title}' in 720p to {output_path} ...")
    stream.download(output_path=output_path)
    print("Download completed successfully.")
else:
    print("480 video not available for this video.")