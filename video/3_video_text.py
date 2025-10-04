from pytubefix import YouTube
from moviepy import VideoFileClip
import speech_recognition as sr_lib  # Use distinct alias to avoid conflict
import librosa
import soundfile as sf
import numpy as np
import os

# Fixed YouTube video URL
url = "https://www.youtube.com/watch?v=EFsmGhXuSZ4"
mp3_file = "a_output.mp3"
wav_file = "temp_audio.wav"
text_file = "transcription.txt"

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
    
    # Convert MP3 to WAV and split into chunks using librosa
    print('Converting MP3 to WAV for transcription...')
    # Load MP3 with librosa
    y, sample_rate = librosa.load(mp3_file, sr=16000, mono=True)  # Mono, 16 kHz for Google API
    sf.write(wav_file, y, sample_rate, subtype='PCM_16')
    print(f"WAV saved as '{wav_file}'")
    
    # Split into 60-second chunks
    print('Transcribing audio to text...')
    chunk_length = 60  # seconds
    samples_per_chunk = chunk_length * sample_rate
    chunks = [y[i:i + samples_per_chunk] for i in range(0, len(y), samples_per_chunk)]
    
    recognizer = sr_lib.Recognizer()  # Use sr_lib to avoid conflict
    text = ""
    for i, chunk in enumerate(chunks):
        chunk_file = f"chunk_{i}.wav"
        sf.write(chunk_file, chunk, sample_rate, subtype='PCM_16')
        with sr_lib.AudioFile(chunk_file) as source:
            audio_data = recognizer.record(source)
            try:
                chunk_text = recognizer.recognize_google(audio_data)
                text += chunk_text + " "
                print(f"Transcribed chunk {i+1}/{len(chunks)}")
            except sr_lib.UnknownValueError:
                print(f"Chunk {i+1}: Could not understand audio.")
            except sr_lib.RequestError as e:
                print(f"Chunk {i+1}: API error: {e}")
        os.remove(chunk_file)
        print(f"Removed temporary chunk file '{chunk_file}'")
    
    # Save transcription
    if text.strip():
        with open(text_file, 'w', encoding='utf-8') as f:
            f.write(text.strip())
        print(f"Transcription saved as '{text_file}'")
    else:
        print("No transcription generated.")
    
    # Clean up temporary WAV file
    if os.path.exists(wav_file):
        os.remove(wav_file)
        print(f"Removed temporary WAV file '{wav_file}'")
else:
    print("360p video not available for this video.")