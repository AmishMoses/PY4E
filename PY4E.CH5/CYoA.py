#!/usr/bin/bash
inventory = []
print("Welcome to the game")
name = "Alex" #input("What is your name: "
print(f"Okay {name}, your wake up in a dark room. You have no source of light around you and feel the cold stone on your back.")

print("\nWhat do you do?")
choices = ['Feel around in darkness', 'Search your pockets']
print(choices)
c1 = input("Choose wisely: 1 or 2 ")
if c1 == "1":
    print("You touch something wet. You hear the low rumbles of growling right before your blood can be felt leaving your body. Whatever it was-was hungry")
    print("Game Over")
elif c1 == "2":
    print("\nYou found a lighter!")
    inventory.append('lighter')
    print("Current inventory:" ,inventory)
light = input("\nWould you like to use your inventory? ")
if light == "yes":
    print("You see a monster. It seems the light was just enought to stir him from his sleep. You feel his claws grasp you as the room goes dark again.")
