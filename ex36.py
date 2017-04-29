# CATCHIN SOME UNREAL AIR
# A GAME BY SHELBY
# THE GOAL OF THIS GAME IS TO DUNK UPON THE BIG MAN
# WITH WHOM THE CARTOON CHARACTERS 'SWEET BRO' AND 'HELLA JEFF'
# ONCE PLAYED A GAME OF BASKETBALL

from sys import exit



# part where you check input against string length:
# we will either send the player to the intro on the second puzzle,
# or send them to the intro of the first puzzle
def firstCheck():
    print "YOU NEED TO WORFMK YOUR .... FEET"
    choice = raw_input("8:y ")
    if choice.length == 32:
        print "Hecp. Your SWEET FOOTWORK is that's got you to"
        print "DUNKEN,, DISTANCE"
        score += 413
        secondIntro()
    else:
        print "you need to see the BIG MAN'S stop your steps"
        print "aaa hellla he's too nimble for you"
        print "So godam . . . slick"
        firstIntro()
# end
