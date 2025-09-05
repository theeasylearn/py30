import pyttsx3

def text_to_speech(text, rate=200, volume=1.0, voice_index=0):
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Get available voices
    voices = engine.getProperty('voices')
    
    # Select a voice (0 for default, can try 1, 2, etc., based on available voices)
    engine.setProperty('voice', voices[voice_index].id)
    
    # Set speech rate (default is 200, lower is slower, higher is faster)
    engine.setProperty('rate', rate)
    
    # Set volume (0.0 to 1.0)
    engine.setProperty('volume', volume)
    
    # Convert text to speech
    engine.say(text)
    engine.runAndWait()

# Example usage
if __name__ == "__main__":
    # Basic example
    # text_to_speech("Hello! This is a text-to-speech demo using pyttsx3.")
    text_to_speech("""
        Twinkle, twinkle, little star,
        How I wonder what you are!
        Up above the world so high,
        Like a diamond in the sky.

        Twinkle, twinkle, little star,
        How I wonder what you are!""")
    
    # Example with different settings
    # text_to_speech("This is slower and quieter.", rate=150, volume=0.8, voice_index=0)