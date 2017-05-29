# PBT stands for 'Please Build This' and stands for things I need to do!
from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print "This scene isn't configured! Subclass it and implement enter()."
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Menu(Scene):

    def enter(self):
        print "WELCOME TO ZED'S GAME"
        print "A TEXT ADVENTURE GAME FOR THE ASPIRING PYTHON PROGRAMMER"
        print """
        INSTRUCTIONS:
        TYPE IN A TEXT COMMAND WHEN YOU SEE A > AT THE END OF TEXT.
        FOR INSTANCE, AT THE END OF THIS TEXT BLOCK!
        COMMANDS ARE NOT CASE-SENSITIVE.
        TYPE 'START' TO START THE GAME. TYPE 'CREDITS' TO SEE THE CREDITS.
        TYPE 'EXIT' TO EXIT THE GAME.
        """

        action = raw_input("> ").lower()

        if action == 'start':
            return 'central_corridor'

        elif action == 'credits':
            print "ZED'S GAME"
            print "Designed by Zed A. Shaw"
            print "Written by Zed A. Shaw, Shelby Donahue, ky, and monkeysky"
            print "Coded on Python 2.7"
            print "Escape Pod puzzle testing by ky and monkeysky"
            print "Quotes from:"
            print "Bertrand Russell"
            print "@Dril"
            print "Jose Canseco \n"
            return 'menu'
        elif action == 'exit':
            exit(0)
        else:
            print "PLEASE TYPE 'START', 'CREDITS', OR 'EXIT', AS THOSE ARE"
            print "THE ONLY COMMANDS AVAILABLE RIGHT NOW."
            return 'menu'



class Death(Scene):

    quips = [
    "'War does not determine who is right - only who is left.' - Bertrand Russell",
    "'\"dont tax me obama.  im dead\" -our beloved dead soldiers' - @dril",
    "'I am and will always be just simply a basball player,my tomb stone will just say.  Baseball' - Jose Canseco",
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print "You are in the central corridor of the space ship."
        print "The corridor is narrow, and covered with doors."
        print "It also has some alien making sounds at you."
        print "The alien is waving an implement at you."
        print "It kind of looks like, I dunno, a grill lighter. \n"

        action = raw_input("> ")

        if action == "shoot":
            print "Your weapons are useless against him!"
            print "The alien has no powers, but can skip reasonably well."
            print "His skipping enrages you, and you have a stroke."
            print "You die of pure anger. \n"
            return 'death'

        elif action == "dodge":
            print "Like a world class boxer you dodge, weave, slip and slide right."
            print "Unfortunately, your expert dodging slams your head against"
            print "a poorly sealed airlock."
            print "You vanish out into space. \n"
            return 'death'

        elif action == "tell a joke":
            print "Lucky for you they taught you Gothon insults in the academy."
            print "You tell the one Gothon joke you know:"
            print "Lbhe zbgure vf fb sng, jur fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr."
            print "The Gothon laughs so heartily and merrily that he can no longer move."
            print "Safely incapacitated, you run past him and jump through the Weapon Armory door. \n"
            return 'laser_weapon_armory'

        else:
            print "DOES NOT COMPUTE!"
            print "(Consider doing, uh, something aggressive. Like attacking."
            print "Or dodging. Or try and break the ice with a joke?) \n"
            return 'central_corridor'


class LaserWeaponArmory(Scene):

    def enter(self):
        print "You do a dive roll into the Weapon Armory, crouch and scan the room"
        print "for more Gothons that might be hiding. It's dead quiet, too quiet."
        print "You stand up and run to the far side of the room and find the"
        print "neutron bomb in its container. There's a keypad lock on the box"
        print "and you need the code to get the bomb out. If you GUESS the CODE"
        print "wrong 10 times the lock closes forever and you can't"
        print "get the bomb. At the advice of your ship's Information Security"
        print "department, the code is a randomly generated 3 digit number that"
        print "nobody, not even the ship's captain, knows. For added security,"
        print "the program is written in Python, which has absolutely no"
        print "vulnerabilities related to input parameters. \n"
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        vuln = "guess = code"
        guess = raw_input("[keypad]> ")
        guesses = 0

        while (guess != code and guesses < 9) and (guess != vuln and guesses < 9):
            print "BZZZZEDDD!"
            guesses += 1
            guess = raw_input("[keypad]> ")

        if guess == code or guess == vuln:
            print "The container clicks open and the seal breaks, letting gas out."
            print "You grab the neutron bomb and run as fast as you can to the"
            print "bridge where you must place it in the right spot. \n"
            return 'the_bridge'
        else:
            print "The lock buzzes one last time and then you hear a sickening"
            print "melting sound as the mechanism is fused together."
            print "You sit there staring at the lock as the Gothons destroy the ship,"
            print "but the bitterness of your impending death is mitigated"
            print "by your admiration for the InfoSec department. With your dying"
            print "breath, you bless the concept of security through obscurity. \n"
            return 'death'

class TheBridge(Scene):

    def enter(self):
        print "You burst onto the Bridge with the neutron destruct bomb"
        print "under your arm and surprise 5 Gothons who are trying to"
        print "take control of the ship. Each of them has an even uglier"
        print "clown constume than the last. They haven't pulled their"
        print "weapons out yet, as they see the active bomb under your"
        print "arm and don't want to set it off. \n"

        action = raw_input("> ")

        if action == "throw the bomb":
            print "In a panic you throw the bomb at the group of Gothons"
            print "and make a leap for the door. Right as you drop it a"
            print "Gothon shoots you in the back killing you."
            print "As you die you see another Gothon frantically try to disarm"
            print "the bomb. You die knowing they will probably blow up when"
            print "it goes off. \n"
            return 'death'

        elif action == "slowly place the bomb":
            print "You point your blaster at the bomb under your arm"
            print "and the Gothons put their hands up and start to sweat."
            print "You inch backward to the door, open it, and then carefully"
            print "place the bomb on the floor, pointing your blaster at it."
            print "You then jump back through the door, punch the close button"
            print "and blast the lock so the Gothons can't get out."
            print "Now that the bomb is placed you run to the escape pod to"
            print "get off this tin can. \n"
            return 'escape_pod'

        else:
            print "DOES NOT COMPUTE!"
            print "You should probably enter something that involves . . ."
            print "moving the bomb in some way. \n"
            return 'the_bridge'

class EscapePod(Scene):

    def enter(self):
        # Special thanks to ky and monkeysky, who helped me with testing
        # and writing the math puzzle here!
        print "You rush through the ship desperately tring to make it to"
        print "the escape pod before the whole ship explodes. It seems like"
        print "hardly any Gothons are on the ship, so your run is clear of"
        print "interference. You get to the chamber with the escape pods, and"
        print "now need to pick one to take. Some of them could be damaged"
        print "but you don't have time to look. There's four doors each leading"
        print "to a pod, which door do you take? Use these clues to find out!"
        print "(Each pod has a different one-digit number on it, from 1 to 9.)"
        print "(The four doors add up to 17.)"
        print "(No two doors add up to 10.)"
        print "(Two of the doors added together equal the largest door, which happens to be the correct one!) \n"

        good_pod = 8
        guess = raw_input("[door #]> ")

        if int(guess) != good_pod:
            print "You jump into pod %s and hit the eject button." % guess
            print "The pod escapes out into the void of space, then"
            print "implodes as the hull ruptures, crushing your body"
            print "into jam. That's a very harsh punishment for not being"
            print "good at math puzzles! \n"
            return 'death'

        else:
            print "You jump into pod %s and hit the eject button." % guess
            print "The pod easily slides out into space heading to"
            print "the planet below. As it flies to the planet, you look"
            print "back and see your ship implode then explode like a"
            print "bright star, taking out the Gothon ship at the same"
            print "time. You won! \n"

            return 'finished'

class Finished(Scene):

    def enter(self):
        print "You won! Good job."
        return 'menu'


class Map(object):

    scenes = {
    'central_corridor': CentralCorridor(),
    'laser_weapon_armory': LaserWeaponArmory(),
    'the_bridge': TheBridge(),
    'escape_pod': EscapePod(),
    'death': Death(),
    'finished': Finished(),
    'menu': Menu()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('menu')
a_game = Engine(a_map)
a_game.play()
