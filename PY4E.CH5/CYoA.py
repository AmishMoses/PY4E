#!/usr/env/ python
def game():
    def death_note():
        print("I'm sorry, it seems the game was too much for you. In all fairness I heard the developer rigged it to make you die fast so he didn't have to work as hard")
        quit()
    inventory = []
    print("Welcome to the game")
    name = input("What is your name: "
    print(f"Okay {name}, your wake up in a dark room. You have no source of light around you and feel the cold stone on your back.")

    print("\nWhat do you do?")
    choices = ['Feel around in darkness', 'Search your pockets']
    print(choices)
    c1 = input("Choose wisely: [1 or 2] ")
    if c1 == "1":
        print("You touch something wet. You hear the low rumbles of growling right before your blood can be felt leaving your body. Whatever it was-was hungry")
        death_note()
    elif c1 == "2":
        print("\nYou found a lighter!")
        inventory.append('lighter')
        print("Current inventory:" ,inventory)
        light = input("\nWould you like to use your inventory? [yes or no] ")
        if light == "yes":
            print("You see a monster. It seems the light was just enought to stir him from his sleep. You feel his claws grasp you as the room goes dark again.")
            death_note()
            quit()
        else:
            print(f"You stash the {inventory} in your pocket. From now on select 'i' during choices to bring up inventory")
            cheeky = input("Wanna try it now? [press i] ")
            if cheeky == "i":
                print(f"I Told you it would work. Right now you have {inventory} collect more or die quickly")
                print("Actually for now, dieeee")
                death_note()
            else:
                print("\nWell screw you pall, I worked pretty hard on this. Do you have any idea how many nested loops are required in game logic? And what you can't even try out what I worked on?")
                print("Okay pal, bet, I have a plan for you :)")
                print('\nYou now hear someone on the other side of the room stand up.')
                print("They quietly laugh as they smell the air, 'hmmmm, I know where you areeee...' says the voice from accross the room")
                death = input("What would you like to do now? [1: Scream 2: Attempt to find a place to hide i: Inventory] ")
                if death == "1" or "2" or "i":
                    print("\nYou pull out your lighter and light it. Your face gleams in the flame as the monster can be seen opening its' toothy maw. Whatever choices brought you here... You know you made incorrectly..")
                    print("All the while the monster eats your flesh you think, 'Ohh, why did I anger the one true god of this world?' And then everything goes cold")
                    death_note()

game()