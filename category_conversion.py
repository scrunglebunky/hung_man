print("PROGRAM BY ANDREW CHURCH\nANSWER CREATION TOOL v1.0")
def div(length,p=True,end='\n'):
    ans = "@"+"-"*length
    if p: print(ans,end=end)
    return ans

div(25)

def MergeMenu() -> bool:
    div(10)
    print("]This is only to be used if you made the category files in BETA v0.5. So... the developer.")
    file1 = input("]Enter the path of the ANSWERS file:\n>")
    file2 = input("]Enter the path of the CATEGORIES file:\n>")
    
    #OPENING THE TWO FILES
    try:
        with open(file1,"r") as file:
            filea = file.read().split(",")
        with open(file2,"r") as file:
            fileb = file.read().split(",")
    except:
        print("] A file does not exist or is not formatted properly.")
        return False

    #MERGING EVERYTHING
    print("] Files found and loaded! Merging to file1 list...")
    try:
        for i in range(len(filea)):
            filea[i] += "~" + fileb[i]
    except:
        print("] A file was not formatted properly.")
        return False
    
    #SAVING
    print("]  Files merged!\n]  Saving to file1")
    newstring=""
    for item in filea:
        newstring+=item
        newstring+=","
        print(item)
    try:
        with open(file1,"w") as file:
            file.write(newstring)
    except:
        print("]   Something went wrong.")
        return False
    print("]   Success!\n]   Feel free to delete the categories file, as the original file has everything you need!")


def CreateMenu() -> bool:
    #OUTPUT INFORMATION TO KEEP YOU IN THE LOOP
    div(10)
    newstring = ""
    add = "~"
    print("]Input as many phrases as you would like!")
    print("] There can be any characters, numbers, letters, whatever you want.")
    print("] !!EXCEPT!! FOR TILDE (~) AND COMMA (,). It is reserved for CATEGORIES AND SEPARTION.")
    print("]To finish, input nothing.")
    print("]To add categories, select 2 at the main menu.")
    #TAKING INPUTS FOR EVERYTHING POSSIBLE
    while add != "":
        add = input("> ",)
        add.replace("~","");add.replace(",","")
        newstring+=(add+",") if add != '' else ''
        print(']Added.');div(5)
    newstring=newstring[:len(newstring)-1]
    div(10)
    #SAVING TO FILE
    try:
        with open(input("]Enter file name (.txt is added by default)\n> ")+".txt","w") as raw:
            raw.write(newstring)
        print("] Saved!")
    except:
        print("] Something went wrong.")
        return False
    return True
    
    
def AddCategories() -> bool:
    div(10)
    file1 = input("]Enter the file to add categories to!")
    file1load = ""
    newstring = ""
    #OPENING FILE
    try:
        with open(file1,"r") as raw:
            file1load = raw.read().split(",")
    except:
        print("] file not found")
        return False

    #ASKING FOR CATEGORIES AS LONG AS NO OTHER CATEGORY EXISTS
    for i in range(len(file1load)):
        div(5)
        if '~' in file1load[i]:
            print("]Category was found! Skipping " + file1load[i] + "...")
            continue
        else:
            file1load[i] += "~" + input("]Enter category for "+file1load[i]+"\n> ")
            continue

    #CONVERTING TO STRING
    for i in range(len(file1load)):
        newstring+=file1load[i]+("," if i < len(file1load)-1 else "")
    #SAVING
    try:
        with open(file1,"w") as raw:
            raw.write(newstring)
        print("] File written and saved!")
    except:
        print("] file not found")
        return False
    
    return True
    

    
def MainMenu() -> bool:
    #LOOPING THROUGH MENU OPTIONS
    div(20)
    choice = input("What would you like to do?\n     (1) Create a new file\n     (2) Add categories to file\n     (3) (LEGACY) Merge category file with answer file\n     (4) Exit\n> ")
    if choice=='1':
        success = CreateMenu()
        return True
    elif choice=='2':
        success = AddCategories()
        return True
    elif choice == '3':
        success = MergeMenu()
        return True
    else:
        return False

run = True
while run:
    run = MainMenu()