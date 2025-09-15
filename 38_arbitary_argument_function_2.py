import asyncio
from googletrans import Translator

async def translate_text(text):
    translator = Translator()
    result = await translator.translate(text, src='en', dest='hi')
    return result.text

async def converter(*words):
    list = []
    for word in words:
        text = await translate_text(word)
        print(f"{word} is converted into gujarti")
        list.append(text)
    return list 
async def main():
    list = await converter('spoon','book','hand','knief','sunset','water')
    print("all words in gujarati")
    for item in list:
        print(item)

asyncio.run(main())
