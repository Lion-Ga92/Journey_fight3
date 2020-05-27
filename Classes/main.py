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
           continue on your path. And after several hours you come across a river Do you stop to fish? or 
           do you give it s wide berth?""")
    dead_horse_choice = input("Do you 'inspect' or do you 'walk away'? ")
    if dead_horse_choice == "inspect":
        print("You inspected the dead horse when a bear attacks you. ")
        print(bcolors.FAIL + bcolors.BOLD + "DEFEND YOURSELF" + bcolors.END)
        fight_creature()
        print("You decided to flay the bear amd, ")
        get_more_potions()
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
            run = False

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
