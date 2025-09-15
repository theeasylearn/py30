import asyncio
from googletrans import Translator

async def translate_text(text):
    translator = Translator()
    result = await translator.translate(text, src='en', dest='hi')
    return result.text

async def main():
    # Example usage of the translate_text function
    text = "Hello, how are you?"
    translated = await translate_text(text)
    print(translated)  # Output: હેલો, તમે કેમ છો?

    # Additional example with different text
    text2 = "Good morning!"
    translated2 = await translate_text(text2)
    print(translated2)  # Output: શુભ સવાર!

if __name__ == "__main__":
    asyncio.run(main())