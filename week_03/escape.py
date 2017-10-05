import pyglet
import time

global answer1
global answer2
global answer3
global answer4
global darkLaugh


darkLaugh = pyglet.media.load("/Users/margarita/Documents/SVA IXD/Slow Code/03_Week/darkLaugh.wav", streaming=False)
exitCode = "3465"

def printGraphic (name):
    if (name == "escapeText"):
        print '                                                                                   '
        print '____________________________________WELCOME TO_____________________________________'
        print '                                                                                   '
        print '      ___           ___           ___           ___           ___         ___      '
        print '     /\__\         /\__\         /\__\         /\  \         /\  \       /\__\     '
        print '    /:/ _/_       /:/ _/_       /:/  /        /::\  \       /::\  \     /:/ _/_    '
        print '   /:/ /\__\     /:/ /\  \     /:/  /        /:/\:\  \     /:/\:\__\   /:/ /\__\   '
        print '  /:/ /:/ _/_   /:/ /::\  \   /:/  /  ___   /:/ /::\  \   /:/ /:/  /  /:/ /:/ _/_  '
        print ' /:/_/:/ /\__\ /:/_/:/\:\__\ /:/__/  /\__\ /:/_/:/\:\__\ /:/_/:/  /  /:/_/:/ /\__\ '
        print ' \:\/:/ /:/  / \:\/:/ /:/  / \:\  \ /:/  / \:\/:/  \/__/ \:\/:/  /   \:\/:/ /:/  / '
        print '  \::/_/:/  /   \::/ /:/  /   \:\  /:/  /   \::/__/       \::/__/     \::/_/:/  /  '
        print '   \:\/:/  /     \/_/:/  /     \:\/:/  /     \:\  \        \:\  \      \:\/:/  /   '
        print '    \::/  /        /:/  /       \::/  /       \:\__\        \:\__\      \::/  /    '
        print '     \/__/         \/__/         \/__/         \/__/         \/__/       \/__/     '
        print '                                                                                   '
        print '____________________________by: Jennifer && Margarita _____________________________'
        print '                                                                                   '

    if (name == "bookshelf"):
        print '||-------------------------------------------------------||'
        print '||.--.    .-._                        .----.             ||'
        print '|||==|____| |H|___            .---.___|""""|_____.--.___ ||'
        print '|||  |====| | |xxx|_          |+++|=-=|_  _|-=+=-|==|---|||'
        print '|||==|    | | |   | \         |   |   |_\/_|Black|  | ^ |||'
        print '|||  |    | | |   |\ \   .--. |   |=-=|_/\_|-=+=-|  | ^ |||'
        print '|||  |    | | |   |_\ \_( oo )|   |   |    |Magus|  | ^ |||'
        print '|||==|====| |H|xxx|  \ \ |''| |+++|=-=|""""|-=+=-|==|---|||'
        print '||`--^----`-^-^---`   `-` ..  `---^---^----^-----^--^---^||'
        print '||-------------------------------------------------------||'
        print '||-------------------------------------------------------||'
        print '||               ___                   .-.__.-----. .---.||'
        print '||              |===| .---.   __   .---| |XX|<(*)>|_|^^^|||'
        print '||         ,  /(|   |_|III|__|..|__|:x:|=|  |     |=| A |||'
        print '||      _a`{ / (|===|+|   |++|  |==|   | |  |Illum| | R |||'
        print '||      `//\/ _(|===|-|   |  |..|  |:x:|=|  |inati| | Y |||'
        print '||_____  -\{___(|   |-|   |  |  |  |   | |  |     | | Z |||'
        print '||       _(____)|===|+|[I]|DK|..|==|:x:|=|XX|<(*)>|=|^^^|||'
        print '||              `---^-^---^--^--`--^---^-^--^-----^-^---^||'
        print '||-------------------------------------------------------||'
        print '||_______________________________________________________||'

    if (name == "monster"):
        #global darkLaugh
        print '              .`````-,              ,-`````.                 '
        print '              `-.._  |              |  _..-`                 '
        print '                 \    `,          ,`    /                    '
        print '                 `=   ,/          \,   =`.                   '
        print '                 `=   (            )   =`.                   '
        print '                .\    /            \    /.                   '
        print '               /  `,.`              `.,`  \                  '
        print '               \   `.                ,`   /                  '
        print '                \    \              /    /                   '
        print '                 \   .`.  __.---. ,`.   /.                   '
        print '                  \.` .```        `. `./.                    '
        print '                   \.`  -```-..     `./                      '
        print '                   /  /        `.      \                     '
        print '                  /  / .--  .-````      `.                   '
        print '                 .   |    ,---.    _      \                  '
        print '     /``-----._.-.   \   / ,-. .-.  `.   .-._.-----``\       '
        print '     \__ .     | :    `., ((O))   ,-.  \  : |     . __/.     '
        print '      `.  `-...\_`     |   `-`   ((O)) |  ._/...-`  ..       '
        print ' .----..)    `    \     \      /  `-`  / /    `    (..----.  '
        print '(o      `.  /      \     \    /\     .` /      \  .`      o) '
        print ' ```---..   `.     /`.    `--`  `---` .`\     .`   ..---```. '
        print '         `-.  `.  /`.  `.           .` .`\  .`  .-`          '
        print '            `..` /   `.`  ` - - - ` `.`   \ `..`             '
        print '                /    /                \    \                 '
        print '               /   ,`                  `.   \                '
        print '               \  ,``.                .``.  /                '
        print '                `/    \              /    \`                 '
        print '                 ,=   (              )   =,                  '
        print '                 ,=   `\            /`   =,                  '
        print '                 /    .`            `.    \                  '
        print '              .-```  |                |  ```-.               '
        print '              `......`                `......`               '
        darkLaugh.play()
        time.sleep(5)

    if (name == "youWin"):
        print '                  ___           ___                    ___                       ___           '   
        print '                 /\  \         /\  \                  /\  \                     /\  \          '
        print '      ___       /::\  \        \:\  \                _\:\  \       ___          \:\  \         '
        print '     /|  |     /:/\:\  \        \:\  \              /\ \:\  \     /\__\          \:\  \        '
        print '     :|  |    /:/  \:\  \   ___  \:\  \            _\:\ \:\  \   /:/__/      _____\:\  \       '
        print '    |:|  |   /:/__/ \:\__\ /\  \  \:\__\          /\ \:\ \:\__\ /::\  \     /::::::::\__\      '
        print '  __|:|__|   \:\  \ /:/  / \:\  \ /:/  /          \:\ \:\/:/  / \/\:\  \__  \:\~~\~~\/__/      '
        print ' /::::\  \    \:\  /:/  /   \:\  /:/  /            \:\ \::/  /   ~~\:\/\__\  \:\  \            '
        print ' ~~~~\:\  \    \:\/:/  /     \:\/:/  /              \:\/:/  /       \::/  /   \:\  \           '
        print '      \:\__\    \::/  /       \::/  /                \::/  /        /:/  /     \:\__\          ' 
        print '       \/__/     \/__/         \/__/                  \/__/         \/__/       \/__/          ' 

def introStory():
    # intro narrative
    # let's introduce them to our world
    print "Good to see you again! What should I call you?"
    playerName = raw_input("Please enter your name > ")

    # intro story, quick and dirty (think star wars style)
    print playerName + ". " + "It is 2:49am, you are sleeping alone. Dreaming about ..."
    raw_input("press enter >")
    print "You hear an eerie sound, and surprisingly loud as well."
    raw_input("press enter >")
    print "Although you want to get up and check it out, you are a bit scared and tired"
    raw_input("press enter >")
    print "so you ignore it by hiding under the covers."
    raw_input("press enter >")
    print "But, suddenly, you see a strange shadow ..."
    raw_input("press enter >")
    print "You sprint to open the door."
    raw_input("press enter >")
    print "Oh no, the door is locked. You need four digits number code to open the lock."
    print "Do you want to look for the clues?" 
    raw_input("press enter >")
    
    pcmd = raw_input("please choose yes or no > ")

    # the player can choose yes or no
    if (pcmd == "yes"):
        print "Let's look underneath the bed."
        raw_input("press enter >")
        bedroomLocation()
    else:
        printGraphic("monster")


def bedroomLocation():
    global answer1

    print "You found a piece of paper. Let's solve the problem: "
    # first question
    print "It's dark. You have ten grey socks and ten blue socks you want to put into pairs."
    print "All socks are exactly the same except for their color."
    print "How many socks would you need to take with you to ensure you had at least a pair?"
    
    answer1 = raw_input("Enter the first digit: ")
    print "Let's look into the closet for the second clue."
    raw_input("press enter >")
    closetLocation()

def bedroomLocationRecap():
    global answer1

    # first question
    print "It's dark. You have ten grey socks and ten blue socks you want to put into pairs."
    print "All socks are exactly the same except for their color."
    print "How many socks would you need to take with you to ensure you had at least a pair?"
    
    answer1 = raw_input("Enter the first digit: ")
    confirmStep()

def closetLocation():
    global answer2

    # second question
    print "What's the next number?"
    print "53, 53, 40, 40, 27, 27, ?"
    
    answer2 = raw_input("Enter the last digit: ")
    print "Great, you have two more to go, look closer at the window."
    raw_input("press enter >")
    windowLocation()

def closetLocationRecap():
    global answer2

    # second question
    print "What's the next number?"
    print "53, 53, 40, 40, 27, 27, ?"
    
    answer2 = raw_input("Enter the last digit: ")
    confirmStep()


def windowLocation():
    global answer3
    # third question
    print "1 + 5 = 12"
    print "2 + 10 = 24"
    print "3 + 15 = 36"
    print "5 + 25 = ?"
    
    answer3 = raw_input("Enter the first digit: ")
    print "One last clue. Let's look at the bookshelf."
    raw_input("press enter >")
    bookshelfLocation()

def windowLocationRecap():
    global answer3
    # third question
    print "1 + 5 = 12"
    print "2 + 10 = 24"
    print "3 + 15 = 36"
    print "5 + 25 = ?"
    
    answer3 = raw_input("Enter the first digit: ")
    confirmStep()

def bookshelfLocation():
    global answer4
    # forth question
    print "How many letter 'a' do you see in the bookshelf?"
    printGraphic("bookshelf")
    
    answer4 = raw_input("Enter the last digit: ")
    confirmStep()


def confirmStep():
    print "You entered:"
    code = answer1 + answer2 + answer3 + answer4
    print code
    print "Is this correct? "
    pcmd = raw_input("Please enter 'yes' or 'no': ")
    if (pcmd == "yes"):
        print "Are you sure? "
        pmcd2 = raw_input("Enter 'yes' or 'no': ")

        if (pmcd2 == "yes"):
            if (code == exitCode):
                printGraphic ("youWin")
            else:
                printGraphic("monster") 
                print "Monster is OUT!"
                darkLaugh.play()

        else:
            print "Where do you want to look at?" 
            roomSelection = raw_input("Enter: 'bedroom' 'closet' 'window' or 'bookshelf'")
            if (roomSelection == "bedroom"):
                bedroomLocationRecap()

            elif (roomSelection == "closet"):
                closetLocationRecap()
            elif (roomSelection == "window"):
                windowLocationRecap()
            else: 
                roomSelection == "bookshelf"
                bookshelfLocation()

    else: 
        pcmd == "no"
        print "Go back to the rooms" 
        roomSelection = raw_input("Enter: 'bedroom' 'closet' 'window' or 'bookshelf' ")
        if (roomSelection == "bedroom"):
            bedroomLocationRecap()

        elif (roomSelection == "closet"):
            closetLocationRecap()
        elif (roomSelection == "window"):
            windowLocationRecap()
        else: 
            roomSelection == "bookshelf"
            bookshelfLocation()

def main():
    printGraphic ("escapeText")
    introStory() # start intro

main() # game starts
