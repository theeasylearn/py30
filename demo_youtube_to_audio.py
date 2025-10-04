from pytubefix import YouTube
from pydub import AudioSegment
import playsound
import os
import time

# Step 1: Take YouTube video URL as input
url = input("Enter YouTube video URL:  ")
mp3_file = "a_output.mp3"

# Step 2: Download YouTube video to current folder with retry logic
max_retries = 3
retry_delay = 5  # seconds

for attempt in range(max_retries):
    try:
        print(f"Connecting to YouTube (Attempt {attempt + 1}/{max_retries})...")
        yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)

        # Try resolutions in order: 720p, 480p, 360p
        resolutions = ["720p", "480p", "360p"]
        stream = None

        for res in resolutions:
            stream = yt.streams.filter(res=res, progressive=True, file_extension='mp4').first()
            if stream:
                print(f"Found {res} stream for '{yt.title}'")
                break

        # If no progressive stream is found, fall back to the first available progressive MP4 stream
        if not stream:
            stream = yt.streams.filter(progressive=True, file_extension='mp4').first()

        if not stream:
            raise Exception("No suitable video stream with audio available.")

        # Download to current folder (output_path="" defaults to current directory)
        output_path = ""
        print(f"Downloading '{yt.title}' in {stream.resolution or 'best available resolution'} to current folder...")
        downloaded_file = stream.download(output_path=output_path, filename="temp_video")
        print("Video download completed successfully.")
        break  # Exit retry loop on success
    except Exception as e:
        if attempt < max_retries - 1:
            print(f"Error downloading video: {e}. Retrying in {retry_delay} seconds...")
            time.sleep(retry_delay)
        else:
            print(f"Error downloading video after {max_retries} attempts: {e}")
            exit(1)

# Step 3: Extract audio and convert to MP3 using pydub
try:
    print('Converting video to MP3...')
    audio = AudioSegment.from_file(downloaded_file, format="mp4")
    audio.export(mp3_file, format="mp3")
    print('MP3 generated')
except Exception as e:
    print(f"Error converting to MP3: {e}")
    if os.path.exists(downloaded_file):
        os.remove(downloaded_file)  # Clean up temp file in case of error
    exit(1)

# Step 4: Remove temporary video file
try:
    if os.path.exists(downloaded_file):
        os.remove(downloaded_file)
    print(f"Saved as {mp3_file}")
except Exception as e:
    print(f"Error removing temporary file: {e}")

# Step 5: Play the audio
try:
    print(f"Playing {mp3_file}...")
    playsound.playsound(mp3_file)
    print("Playback complete")
except Exception as e:
    print(f"Error playing audio: {e}")