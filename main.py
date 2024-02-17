import pygame,math,os,sys,random

window = pygame.display.set_mode((600,400),pygame.SCALED)
winrect = window.get_rect()
clock = pygame.time.Clock()
run=True;fps=60;next=60
pygame.font.init()
import anim,backgrounds
from audio import play_song,playsound,playtiedsound
from anim import all_loaded_images as img



fx = pygame.sprite.Group()
#background asset
bg = backgrounds.Background(img="hangmanbg.png",resize=winrect.size,speed=(1,1))
#information
intermission = 0 
#loading text and information relating to it
def pick_random_text() -> tuple:
    textlist_name = random.choice(os.listdir('./textlists/'))
    # textlist_name = "cis.txt"
    #picking text piece
    with open('./textlists/'+str(textlist_name),"r") as raw:
        textlist = raw.read().split(",")
        index = random.randint(0,len(textlist)-1)
        text = textlist[index]
        category = "NONE"
        #picking a category
        for i in range(len(text)):
            if text[i] == "~":
                category = text[i+1:]
                text = text[:i]
                break
        #default category
        if category == "NONE":
            category = textlist_name
    return text,category



#hangman asset
class HangMan():
    def __init__(self):
        self.lynch = anim.AutoImage(self,"lynch.png",generate_rect=False)
        self.tries = -1 
        self.dead = False
        #showing images
        self.show = [False for i in range(6)]
        #body part photos
        self.parts = []
        self.parts.append(anim.AutoImage(self,random.choice(list(anim.headlist.keys())),resize=(50,50),generate_rect=False))
        self.parts.append(anim.AutoImage(self,"default_body",current_anim="body",resize=(50,50),generate_rect=False))
        self.parts.append(anim.AutoImage(self,"default_body",current_anim="larm",resize=(50,50),generate_rect=False))
        self.parts.append(anim.AutoImage(self,"default_body",current_anim="rarm",resize=(50,50),generate_rect=False))
        self.parts.append(anim.AutoImage(self,"default_body",current_anim="lfoot",resize=(50,50),generate_rect=False))
        self.parts.append(anim.AutoImage(self,"default_body",current_anim="rfoot",resize=(50,50),generate_rect=False))
        #positions
        self.poses = ([60,75],[60,135],[10,125],[110,125],[50,175],[70,175])
        self.pos = [0,0]

    def update(self):
        self.lynch.update()
        for item in self.parts:
            item.update()
    
    def draw(self,window):
        window.blit(self.lynch.image,self.pos)
        for i in range(len(self.show)):
            if self.show[i]:
                window.blit(self.parts[i].image,(self.poses[i][0]+self.pos[0],self.poses[i][1]+self.pos[1]))
    
    def update_tries(self):
        #updating dying parts and adding endgame stuff
        self.tries += 1
        self.dead = self.tries >= len(self.show)-1
        if self.tries < len(self.show):
            self.show[self.tries] = True



#game asset
class Game():

    font = pygame.font.Font("./data/comicsans.ttf",20)
    #alphabet information
    alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
    special = "!@#$%^&*()_+-=1234567890[]{}\\|:;<>?,./\"\'"
    alphabet_loaded = {}
    for i in alphabet:
        alphabet_loaded[i] = font.render(i,False,(128,0,0))
    for i in special:
        alphabet_loaded[i] = font.render(i,False,(128,0,0))
    #the underscore
    underscore = img['underscore.png']


    def __init__(self,text,category:str="NONE"):
        self.hangman = HangMan()
        self.win = None #True if win, False if loss, None if game is still 
        self.tried_letters = "" #what letters have been attempted
        self.succeeded_letters = "" #what letters have MATCHED 
        self.original = str(text).upper() #the original bit of text put in, used for displaying it to the screen
        #the original text but with special characters removed, for matching purposes
        self.match = "" 
        for i in self.original:
            if i in Game.alphabet:
                self.match += i
        #current letter input
        self.letter = ""
        #details to show
        self.category = category
        self.G_category=Game.font.render("CATEGORY: " + self.category,color="white",bgcolor="black",antialias=False)
        


    def draw(self,window):
        self.hangman.draw(window)

        #drawing characters and correctly guessed ones
        placement = [0,325]
        for i in range(len(self.original)):
            #drawing the underscore for the letter bitk
            if self.original[i] in Game.alphabet:
                window.blit(Game.underscore,placement)
                #drawing the characters
                if self.original[i] in self.succeeded_letters:
                    window.blit(Game.alphabet_loaded[self.original[i]],(placement[0],placement[1]-5))
            #drawing special characters that don't get guessed
            elif self.original[i] in Game.special:
                window.blit(Game.alphabet_loaded[self.original[i]],placement)
            #space newline
            if self.original[i] == " " and placement[0] > winrect.width*.75:
                placement[0] = 0
                placement[1] += 25 
            #normal newline
            else:
                placement[0] += 25
                if placement[0] >= winrect.width-20:
                    placement[0] = 0
                    placement[1] += 25 

        
        #drawing failed letters
        placement = [150,10]
        for letter in self.tried_letters:
            window.blit(Game.alphabet_loaded[letter],placement)
            placement[0] += 25 
            if placement[0] >= winrect.width-20:
                placement[1] += 25
                placement[0] = 150
        
        #drawing the right letters if lost
        if self.win == False:
            #drawing characters and correctly guessed ones
            placement = [0,325]
            for i in range(len(self.original)):
                #drawing the underscore for the letter bitk
                if self.original[i] in Game.alphabet:
                    if self.original[i] not in self.succeeded_letters:
                        window.blit(Game.alphabet_loaded[self.original[i]],(placement[0]+random.randint(-1,1),placement[1]-10+random.randint(-1,1)))
                #space placement
                if self.original[i] == " " and placement[0] > winrect.width*.75:
                    placement[0] = 0
                    placement[1] += 20 
                #updating placement if no space
                else:
                    placement[0] += 25
                    if placement[0] >= winrect.width-20:
                        placement[0] = 0
                        placement[1] += 20 

        #Drawing the category and textlist
        placement = [150,100]
        # window.blit(self.G_textlist_name,placement)
        # placement[1] += 20
        window.blit(self.G_category,placement)





    def update(self):
        self.hangman.update()
        if self.win is None: self.check_win()


    def event_handler(self,event):
        if self.win is not None: return
        if event.type == pygame.KEYDOWN:
            #submitting a letter
            self.letter = pygame.key.name(event.key).upper()
            self.submit_letter()
        

    def submit_letter(self):
        #submitting a letter 
        if self.letter not in Game.alphabet:
            pass
        #failed attempt -- already in there
        elif self.letter in self.tried_letters or self.letter in self.succeeded_letters:
            pass
        #failed attempt -- not in word
        elif self.letter not in self.match:
            fx.add(anim.WhiteFlash(surface=window,spd=5,img=random.choice(anim.wronglist)))
            playsound("bad.mp3")
            self.tried_letters += self.letter
            self.hangman.update_tries()
        #succeeded attempt -- word not yet used and in program
        elif self.letter in self.match:
            fx.add(anim.WhiteFlash(surface=window,spd=5,img=random.choice(anim.rightlist)))
            playsound("good.mp3")
            self.succeeded_letters += self.letter
            self.letter = ""
        #resetting letter
        self.letter = ""


    def check_win(self):
        #checking if the hangman says lose
        losscheck = self.hangman.dead
        #checking if there are any letters not in the succeeded lettesr
        wincheck = True
        for i in self.match:
            if i not in self.succeeded_letters:
                wincheck = False
        #updating the game
        if wincheck: self.win = True
        if losscheck: self.win = False




#game object
text,category = pick_random_text()
game = Game(text=text,category=category)




while run:
    #updating everything
    bg.update()
    bg.draw(window)
    game.update()
    game.draw(window)
    fx.update()
    fx.draw(window)


    #intermission start code
    if (game.win is not None) and intermission == 0 :
        if game.win:
            fx.add(anim.WhiteFlash(window,spd=1.0,img="confetti"))
            playtiedsound("confetti")
        else:
            ...
        #playing sounds or an effect or whatever
        intermission += 1
    #intermission code
    elif (game.win is not None) and intermission < 360:
        if intermission%next==0:
            id = random.choice(anim.winlist if game.win else anim.loselist)
            fx.add(anim.WhiteFlash(window,spd=5.0,img=id))
            playtiedsound(id)   
            next=random.choice((15,20,30,45,50,60))
        intermission += 1
    #new game
    elif (game.win is not None):
        text,category = pick_random_text()
        game = Game(text=text,category=category)
        intermission = 0




    #basic timer and controls
    clock.tick(fps)
    pygame.display.update()
    for event in pygame.event.get():
        game.event_handler(event)
        if event.type == pygame.QUIT:
            run=False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # print(game.original)
                pass
            elif event.key == pygame.K_ESCAPE:
                run=False
            elif event.key == pygame.K_1:
                pygame.display.toggle_fullscreen()

    #music
    if not pygame.mixer.music.get_busy():
        play_song()
