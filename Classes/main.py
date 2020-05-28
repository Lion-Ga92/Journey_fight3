from sys import exit
from Classes.game import bcolors, Person, Creature

print("Hello and welcome to your journey, today we will go across a a forest path and we may encounter enemies.")
print("Keep an eye on the hints, which will affect the story as you go along. You may be attacked at random.")
print("When you enter a battle, you will be given three choices either 'fight', 'heal', 'rum'")
print("When you are in battle mode, you will not be able to exit the script. Only when making decisions will you be ")
print("able to type 'quit' as an input and exit the script. Play out the battle before attempting to quit.")
input("Press enter to continue")

player = Person(400, 40, 10, 10, 10)
enemy = Person(400, 40, 10, 5, 10)
enemy2 = Person(400, 50, 10, 5, 10)
Bear = Creature(100, 40)


def start_journey():
    print("""You are walking down a forest, in the realms of Gaul. You are on the way to the Feast of Augustus,
          As you approach a fork in the road, you noticed there is no signage. You pause to think, and see both 
          roads. The left most road seems to be wide and appealing, it seems to be the main road. But you hesitate 
          to take it as robbers and pillagers tend to stake them out. The right road seem harder to walk through, 
          the terrain in rough. And the trees are less wide apart than the right path. But you hope that as the less
          busy one robbers will be less of a concern.""")
    input("press enter to continue")
    start_choice = input("Do you take the 'left' road or the 'right' road? Please type choice in single quotes: ")
    if start_choice == "left":
        print("Well the left road seems easier to walk through, you are well armed and can take care of your self")
        print("You walk down the road for a couple hours, when you are attacked by a robber.")
        print(bcolors.FAIL + bcolors.BOLD + "A battle ensues" + bcolors.END)
        print("fight")
        do_battle()
        you_continue()

    elif start_choice == "right":
        print("You took the right most road and start on your journey. The terrain is rough and unhewm and quite eerie")
        print("""But you keep pressing on ahead and come upon a river, the river seems shallow and fast. You are a 
              a strong person and are sure you can swim it""")
        river_cross()

    elif start_choice == "quit":
        print("You have quit the game, you will not be able to return to this choice unless you take the same path. ")
        exit()

    else:
        print("Response not valid")
        print(bcolors.FAIL + bcolors.BOLD + "Restarting from current decision point" + bcolors.END)
        start_journey()



def you_continue():
    print("""Phew, that was a hard battle. It was well fought and after a day of resting and drinking healing
           potions you continue on your path hoping the new day does not bring any unpleasant surprises.
           at any rate. You have plenty of potions. Which though small in size, are great and powerful healers. You 
           continue on your path. And after several hours you come across a dead horse, Do you stop to inspect it? or 
           do you give it s wide berth?""")
    dead_horse_choice = input("Do you 'inspect' or do you 'walk away'? ")
    if dead_horse_choice == "inspect":
        print("You inspected the dead horse when a bear attacks you. ")
        print(bcolors.FAIL + bcolors.BOLD + "DEFEND YOURSELF" + bcolors.END)
        fight_creature()
        print("You decided to flay the bear and, ")
        get_more_potions()
        input("Press enter to continue")
        print("After you harvested some potions from the bear you continued on your journey and came upon a river")
        print("You crossed the bridge and come upon a fork in the road.")
        fork_in_road()

    elif dead_horse_choice == "walk away":
        print("""You were prudent, and kept walking. God knows what could have killed the horse, so its better to keep going,
               instead of facing what dreadful animal or cruel person could have done such a deed. Having to fight for your 
               life once is enough for one journey. Maybe it was not the best idea to take the main road. Your destination
               should not be too far away though. As the forest is just a day's walk long.""")
        print("""You see a river up ahead, and a small little bridge to cross it. You are feeling a bit hungry, so it 
              it might be a good idea to stop and fish for a bit. """)
        fishing_choice = input("Do you 'fish' or 'walk across' brige? Remember to keep input to choices in quotes")
        if fishing_choice == "fish":
            get_more_potions()
            cont_after_fishing_1()

    elif dead_horse_choice == "quit":
        print("You have quit the script, good bye. You will start your journey from the start when running script again")
        exit()

    else:
        print("Response not valid")
        print(bcolors.FAIL + bcolors.BOLD + "Restarting from current decision point" + bcolors.END)
        you_continue()

def river_cross():
    print("You start swimming across the river, it is a tough going.")
    print("The current is strong and hard to stay afloat, but you are halfway across.")
    print("Unfortunately you are tiring out and are near the point of drowning")
    print("You keep struggling on...")
    input("Press enter")
    print("It is getting nearly impossible")
    input("Press enter")
    print("You start swallowing water")
    input("Press enter")
    print("You drowned")
    exit()
""""
For river_crossing() i want to add other elements after this but i decided to type it like this for the time being 
and close this branch of the decision tree. i want to add elements of potion taking and healing. While slowly moving 
the storyline back to the bridge. Or make it across the river before continuing down the road.
"""
def fork_in_road():
    print("""After a long journey, and a few scary moments. You crossed the bridge and come upon a fork in the road. 
          The journey so far has been tough, and you hope that you will reach your destination on time for the feast 
          of Augustus. In the road you notice that there are two signs. One points to the left and reads 'Lugdunum' 
          and it is the Destination you are heading toward, the other at the right is hard to distinguish as the words 
          are worn down. As you read the signs. You hear a shrill cry from the right road. You think for a second 
          about which path to take?  """)
    fork_road_choice = input("Do you take the 'left' or 'right' path? Please keep your input to 'in quotes' text: ")
    if fork_road_choice == "left":
        print("You ignored the cry from the right road, it is too risky. And you do not know what could happen.")
        input("Press enter...")
        print("After walking for a couple hours, you reach the edge of the forest. And continue on your way...")
        print("""You will make it to the feast of Augustus on time. Thanks for taking this road with us, you may 
              restart your journey and make other choices. Good bye for now.""")
        exit()

    if fork_road_choice == "right":
        print("You are a kind person, and you decide that honor demands that you at least go and search the right road")
        print("""You walk with guarded steps, and your sword on your hand. You slowly come upon a clearing. Where there
              seem to be a burned cart. And some bodies on the ground, and you start to get apprehensive. Suddenly an 
              enemy appears. """)
        enemy.full_restore()
        do_battle()
        go_back_fork()

    if fork_road_choice == "quit":
        print("You have exited the script, you will be taken to the start of your journey when you restart the script")
        print("Good bye")
        exit()

    else:
        print("Response not valid")
        print(bcolors.FAIL + bcolors.BOLD + "Restarting from current decision point" + bcolors.END)
        fork_in_road()


def cont_after_fishing_1():
    print("""After a long journey, and a few scary moments. You crossed the bridge and come upon a fork in the road. 
          The journey so far has been tough, and you hope that you will reach your destination on time for the feast 
          of Augustus. In the road you notice that there are two signs. One points to the left and reads 'Lugdunum' 
          and it is the Destination you are heading toward, the other at the right is hard to distinguish as the words 
          are worn down. As you read the signs. You hear a shrill cry from the right road. You think for a second 
          about which path to take?  """)
    fork_road_choice_1= input("Do you take the 'left' or 'right' path? Please keep your input to 'in quotes' text: ")
    if fork_road_choice_1 == "left":
        print("You ignored the cry from the right road, it is too risky. And you do not know what could happen.")
        input("Press enter...")
        print("After walking for a couple hours, you reach the edge of the forest. And continue on your way...")
        print("""You will make it to the feast of Augustus on time. Thanks for taking this road with us, you may 
              restart your journey and make other choices. Good bye for now.""")
        exit()

    if fork_road_choice_1 == "right":
        print("You are a kind person, and you decide that honor demands that you at least go and search the right road")
        print("""You walk with guarded steps, and your sword on your hand. You slowly come upon a clearing. Where there
              seem to be a burned cart. And some bodies on the ground, and you start to get apprehensive. Suddenly an 
              enemy appears. """)
        enemy.full_restore()
        do_battle()
        go_back_fork()

    if fork_road_choice_1 == "quit":
        print("You have exited the script, you will be taken to the start of your journey when you restart the script")
        print("Good bye")
        exit()

    else:
        print("Response not valid")
        print(bcolors.FAIL + bcolors.BOLD + "Restarting from current decision point" + bcolors.END)
        fork_in_road()


def go_back_fork():
    print("""My God this forest is infested with Thieves, and dangers. These are not the best times to be alive. The 
          nation of Gaul is facing some difficulties times. But again we have prevailed, and have managed to outwit our 
          foes. After looking around the battle field you conclude that there is no path to be followed from here.""")
    input("Press enter to continue")
    print("""You trace your steps back to the cross sign and take the left road. After a few hours you reach the end
          the forest. And hope that no more scoundrels or creatures await your path.""")
    input("Thank you for joining us in this journey, battles were fought and won with honor. Press enter to leave")
    print("Good bye")
    exit()



def do_battle():
    run = True
    while run:
        print("=================================")
        player.choose_action()
        choice = input("Choose action: ")
        while not choice.isnumeric():
            print("not valid")
            do_battle()
        index = int(choice) -1

        if index == 0 :
            dmg = player.generate_damage()
            enemy.take_damage(dmg)
            print("You attacked for", dmg, "points of damage. Enemy HP:", enemy.get_hp())

            enemy_choice = 0

            enemy_dmg = enemy.generate_damage()
            player.take_damage(enemy_dmg)
            print("Enemy attacks for", enemy_dmg, "Player HP", player.get_hp())

        elif index == 1:
            player.take_potions()
            if player.get_npotions() > 0:
                heal = player.generate_hep()
                player.take_heal(heal)
                print("You took a healing potion for", heal, "Player HP:", player.get_hp())
                print("Potions left:", player.get_npotions(), "/", player.get_max_npotions())

            elif player.get_npotions() < 0:
                print("You cannot take a potion at this time")

            enemy_choice = 1

            enemy.take_potions()
            if enemy.get_npotions() > 0:
                enemy_heal = enemy.generate_hep()
                enemy.take_heal(enemy_heal)
                print("Enemy took a healing potion for", enemy_heal, "Enemy HP:", enemy.get_hp())
                print("Potions left:", enemy.get_npotions(), "/", enemy.get_max_npotions())

            elif enemy.take_potions() < 0:
                print("Enemy ran out of potions. He cannot take any more potions")


        elif index == 2:
            print("You ran away")
            run = False

        if enemy.get_hp() == 0:
            print("Your ememy is dead, you were wounded. We recommend resting to recover hp.")
            print("your total number of potions is", player.get_npotions(), "/", player.get_max_npotions())
            healing_rest = input("Do you want to rest? 'yes' or 'no': ")
            if healing_rest == "yes":
                player.full_restore()
                print("After a day of rest, you recovered your strength to continue walking.")
                run = False
            elif healing_rest == "no":
                print("You continued your path, and died after several hours from the wounds")
                exit()
        elif player.get_hp() == 0:
            print("You died")
            exit()

def fight_creature():
    run = True
    while run:
        print("=================================")
        player.choose_crAction()
        crChoice = input("Choose action: ")
        while not crChoice.isnumeric():
            print("not valid")
            fight_creature()
        index = int(crChoice) - 1

        if index == 0:
            dmg = player.generate_damage()
            Bear.take_damage(dmg)
            print("You attacked for", dmg, "points of damage. Creature HP:", Bear.get_hp())

            enemy_choice = 0

            creature_dmg = Bear.generate_damage()
            player.take_damage(creature_dmg)
            print("Enemy attacks for", creature_dmg, "Player HP", player.get_hp())


        elif index == 1:
            print("You ran away")
            print("The bear gives chase to you, and catches you after a few minutes. It mortally wounds you...")
            print("You are bleeding...")
            input("Press enter")
            print("You lay in agony, the bear comes around again")
            input("Press enter")
            print("It starts to tears you from limb to limb...")
            print("You died horribly as a victim of the bear. Your family never finds your body. ")
            exit()


        if Bear.get_hp() == 0:
            print("The creature is dead, you were wounded. We recommend resting to recover hp.")
            healing_rest = input("Do you want to rest? 'yes' or 'no': ")
            if healing_rest == "yes":
                print("After a day of rest, you recovered your strength to continue walking.")
                run = False
            elif healing_rest == "no":
                print("You continued your path, and died after several hours from the wounds")
                exit()
        elif player.get_hp() == 0:
            print("You died")
            exit()

def get_more_potions():
    plus_potions = player.generate_npotions()
    player.add_potions(plus_potions)
    print("You started searching for potions and got some potions. Your new potions total is", player.get_npotions())

start_journey()
