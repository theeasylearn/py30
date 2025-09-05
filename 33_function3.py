from playsound import playsound
def PlaySound():
    playsound('sound/ding.mp3')
def PlayMySound(filename):
    playsound(filename)
    
PlaySound()
temp = input("Press any key to continue")
PlayMySound('sound/claping.mp3')
temp = input("Press any key to continue")
PlayMySound('sound/breaking.mp3')