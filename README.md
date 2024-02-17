# WELCOME TO HUNGMAN
- This is just a goofy little hangman clone that lets you put whatever images you'd like as lose graphics, win graphics, correc tor incorrect graphics, or even the heads of the hangmen!
- You can even make custom lists! Maybe you'd like to use this for a classroom.
- [DO NOT USE THIS FOR CLASSROOM PURPOSES AS THE GAME IS LOUD AND CHAOTIC]

HOW TO PLAY
- Type an alphabetical character to guess it on the list.
- Numbers, special characters, etc. are given to you for free.
- Get 6 characters wrong and you lose.
- The game loops on infinitely.

GRAPHICS
- There is an "image loadlist" to load unrelated images, but there are separate folders for heads, wins, losses, correct guesses, and incorrect guesses.
- These folders are loaded automatically, so DO NOT PLACE incompatible files in there (i will change this later).
- The game will then plaster a randomly selected image to flash the screen when an event occurs (win, lose, good, bad, self explanatory.)
- A random head is also selected to serve as the head of the hangman. Other images can be added there too.

WINTIE
- A deceptive name, as the losing images also count.
- This is a simple way to link a photo to an image, so when you pick a picture to flash the screen a special sound will play.
- It is VERY EASY to break this due to how specific json files are, so it is best to leave them be. 
- The "correct/incorrect guess" sound is always the buzzer, so these sounds only play with the win/lose event files.

TEXTLISTS
- To add text, place a txt file into the textlists category.
- Each word or phrase needs to be separated with a comma, and the game does not care about any other characters (spaces, special characters, numbers, etc. are okay).
- All special characters are recognized, and if they do not (or they are a space), a blank space will be added, even if it is at the START OR END of the phrase.
- Look at ComputerInformationScience.txt to see what I mean.


CATEGORIES
- In the textlist files, you will notice that some of them will have a tilde (~) followed by another word. This is a category.
- The game splices the text pieces and gives you that part as a hint.
- [answer]~[category]


TOOL TO CREATE TEXTLISTS
- the category_conversions.py tool will let you create the files without adding commas or worrying about formatting
- USE THIS FOR CUSTOM TEXT LISTS
- The second option lets you pick a pre-existing textlist to add categories to it if you have not done it before
- There is currently no option to modify existing sheets, so don't do that.

MUSIC
- The simplest one
- Just drag a song file into the music folder (.mp3,.wav) and let it run.
- Don't be stupid. Longer files will use too much ram.
