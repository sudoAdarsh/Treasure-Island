# Author : Adarsh Upadhyay

import time
import os

logo ='''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/_____"=.o|o_.--""___/______/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
'''

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def cprint (text, speed = 0.035, line_delay = 0.4):
    if isinstance(text, str):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(speed)
        print()
        time.sleep(line_delay)
    elif isinstance(text, list):
        for line in text:
            try:
                for char in line:
                    print(char, end='', flush=True)
                    time.sleep(speed)
            except TypeError:
                print(str(line))
            print()
            time.sleep(line_delay)
    else:
        raise TypeError("cprint only accepts strings or list of strings")

def logo_print():
    clear()
    for line in logo.splitlines():
        print(line)
        time.sleep(0.02)
    time.sleep(0.5)

def get_choice(prompt, options):
    while True:
        choice = input(prompt).lower().strip()
        if choice == "restart":
            main()
        elif choice in options:
            return choice
        else:
            cprint("That doesn't seem right....try again.\n")

def crossroad_scene():
    cprint("\nSCENE 1: THE CROSSROAD\n")
    cprint("Darkness surrounds you. You hear distant waves crashing.", line_delay=1)
    cprint("A fork lies ahead. The left path winds into shadowed woods, the right disappears into a jagged cliff.", line_delay=1.2)
    cprint('You murmur to yourself: "I must choose my path carefully..."\n', line_delay=1)
    
    
    choice = get_choice(">>> Left or Right? \n", ["left", "right"])
    
    if choice == "left":
        cprint("\nYou step cautiously onto the left path. The forest thickens and the scent of damp earth fills your nostrils.", line_delay=1)
        cprint("Eventually, the path opens up to reveal a silvery lake under the moonlight…", line_delay=1.2)
        return "lake"
    else:
        return ("game_over", "\nYou misstep and fall into a pit of spikes! The forest seems to whisper in mockery...")

def lake_scene():
    cprint("\nSCENE 2: MISTY LAKE\n")
    cprint("You arrive at a misty lake. Moonlight dances on the rippling water.", line_delay=1)
    cprint("Something tells you to wait… or perhaps take your chances and swim?\n", line_delay=1)
    
    choice = get_choice(">>> Wait or Swim? \n", ["wait", "swim"])
    
    if choice == "wait":
        cprint("\nYou wait patiently. A small, rickety boat drifts to your side, as if by fate.", line_delay=1.2)
        cprint("You climb aboard and are carried across the misty waters to a small, deserted island.", line_delay=1.2)
        cprint("On the shore, three ancient doors stand, each emanating a strange aura…", line_delay=1)
        return "door"
    else:
        return ("game_over", "\nYou dive into the lake, but sharp jaws snap around you. The water turns red…")

def door_scene():
    cprint("\nSCENE 3: THE FORK\n")
    cprint("You stand before the three doors: Red, Blue, Green.", line_delay=1)
    cprint("*A strange aura seems to hover around each door… choose wisely.*\n", line_delay=1)
    
    choice = get_choice(">>> Red, Blue, or Green? \n", ["red", "blue", "green"])
    
    if choice == "red":
        return ("win", "\nYou open the red door and discover the legendary treasure! 🎉 Gold glimmers everywhere…\n")
    elif choice == "blue":
        return ("game_over", "\nAs you touch the blue door, a dark curse envelops you! You collapse under the witch’s spell…")
    else:  # green
        return ("game_over", "\nThe green door bursts open, and acidic waters engulf you… your journey ends here.")

def game_over_scene(reason):
    cprint(f"Game Over! {reason}\n")
    choice = get_choice("Do you want to restart? (yes/no): ", ["yes", "no"])
    if choice == "yes":
        logo_print()
        return "crossroad"  # restart from beginning
    else:
        cprint("Thanks for playing!\n")
        exit()



def main():
    logo_print()
    cprint("\nDarkness.")
    cprint("Your chest heaves.")
    cprint("Salt burns your throat.")
    cprint("The sound of crashing waves pounds in your ears.")
    cprint("\nAwakening...\n", line_delay= 1.5)
    cprint("\n       TREASURE ISLAND: THE AWAKENING\n")
    cprint("      ...Welcome to Treasure Island...\n", line_delay=0.5)
    cprint("Your mission is to find the Treasure.", line_delay=1.2)
    scene = "crossroad"

    while True:
        if scene == "crossroad":
            scene = crossroad_scene()
        elif scene == "lake":
            scene = lake_scene()
        elif scene == "door":
            scene = door_scene()
        elif isinstance(scene, tuple) and scene[0] == "game_over":
            scene = game_over_scene(scene[1])
        elif isinstance(scene, tuple) and scene[0] == "win":
            cprint(scene[1])
            break

main()