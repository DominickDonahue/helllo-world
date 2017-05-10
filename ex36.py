# CATCHIN SOME UNREAL AIR
# A GAME BY DOORMAKERGAL
# THE GOAL OF THIS GAME IS TO DUNK UPON THE BIG MAN
# WITH WHOM THE CARTOON CHARACTERS 'SWEET BRO' AND 'HELLA JEFF'
# ONCE PLAYED A GAME OF BASKETBALL

from sys import exit

score = 0

def gameStart():
    print """
    UNREAL AIR
    A GAME BY DOORMAKERGAL
    THE GOAL OF THIS GAME IS TO DUNK UPON THE BIG MAN \n
    PRESS ENTER TO BEGIN
    """
    raw_input("8:y ")
    firstIntro()


# part where you check input against string length:
# we will either send the player to the intro on the second puzzle,
# or send them to the intro of the first puzzle

def firstIntro():
    print """
    bro you're in the BIG GAME
    the BIG MAN and you are doing, that ONE-ON-ONE"
    right now .... you HAVV the rock \n
    """
    firstCheck()

def firstCheck():
    print "YOU NEED TO WORFMK YOUR .... FEET"
    choice = raw_input("8:y ")
    # The player needs something with a modulo of 2 when divided by 7
    # for convenience i made it so it has to be longer than 3.
    if (len(choice) % 7 == 2) and len(choice) > 3:
        print "Hecp. Your SWEET FOOTWORK is that's got you to"
        print "DUNKEN,, DISTANCE"
        global score
        score += 413
        secondIntro()
    else:
        print "you need to see the BIG MAN'S stop your steps"
        print "aaa hellla he's %2 nimble for you, "
        print "So godam . . . slick . . ."
        # Wrong inputs reduce your score
        # More obtuse and stupid checks = fewer points subtracted
        score -= 134
        firstIntro()

def secondIntro():
    print """
    yourre driving SO HARD threw the PAINT
    DOWN TOWN!
    AND it's time for . . .
    the FAED
    """
    secondCheck()

def secondCheck():
    print "allhhly oop . . . "
    choice = raw_input("8:y ")
    ploober = choice.lower()
    # here we will check to see if the letters for 'jump' are in the string.
    # they need to appear at least once!
    if 'j' in ploober and 'u' in ploober and 'm' in ploober and 'p' in ploober:
        print "you HAVE it."
        print "that UNREAL AIR"
        global score
        score += 413
        thirdIntro()
    else:
        print "you FALL DOWN"
        print "aah and now , the refs are involved"
        score -= 314
        secondIntro()

def thirdIntro():
    print """
    AAND HERE YOU GOES
    THE PLAYER hass THE ROCK
    coming down on that BASKET BALBASKET
    FOR A
    DUNK
    """
    thirdCheck()

def thirdCheck():
    choice = raw_input("8:y ")
    if choice == "DUNK":
        global score
        score += 413
        print """
        SOCOCRE 8:y \n
        Thank you for playing UNREAL AIR!
        Your score was %d
        """ % (score)
        playAgain()

    else:
        print "YOU GOT TO FLIP IT. DUNK-WAYS"
        score -= 413
        thirdIntro()

def playAgain():
    # A way to quit the game or replay
    global score
    print "Do you want to play again? y/n"
    choice = raw_input("8:y ")
    ploober = choice.lower()
    if ploober == "y":
        score = 0
        firstIntro()
    elif ploober == "n":
        exit(0)
    else:
        print "Type y or n to make your choice."
        playAgain()

# this starts the game!

gameStart()

# If you're reading this, thank you!
