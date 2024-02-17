import pygame,random,os,json

pygame.mixer.init()



#opening soundlist file
loadlist = os.listdir("./sounds/")
loadedlist = {}
for sound in loadlist:
    loadedlist[sound] = pygame.mixer.Sound("./sounds/"+sound)

#opening ties file
with open("./data/win_ties.json","r") as raw:
    win_ties = json.load(raw)


#playing sound
def playsound(name):
    loadedlist[name].play()

def playtiedsound(name):
    #takes a loaded image and tries to see if there is a tied sound to it to play
    if name in win_ties.keys():
        if win_ties[name] in loadlist:
            playsound(win_ties[name])


#music
def play_song():
    pygame.mixer.music.load("./music/"+str(random.choice(os.listdir("./music/"))))
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()
