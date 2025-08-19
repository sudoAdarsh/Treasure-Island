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
/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
'''

intro_lines = [
    "Darkness.\n",
    "Your chest heaves.\n",
    "Salt burns your throat.\n",
    "The sound of crashing waves pounds in your ears.\n",
    "\nAwakening...\n"
]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_logo(art, delay=0.05):
    clear()
    for line in art.splitlines():
        print(line)
        time.sleep(delay)

def cinematic(lines, delay=1.5):
    for text in lines:
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.04)  # typing effect
        time.sleep(delay)

if __name__ == "__main__":
    draw_logo(logo, 0.02)
    time.sleep(1)
    print("\n       TREASURE ISLAND: THE AWAKENING\n")

    start = input("Do you wish to start the game? (Y/n): ").strip().lower()
    if start == "y" or start == "Y":
        clear()
        cinematic(intro_lines, delay=1)
        print("\n...Welcome to Treasure Island...\n")
        print("Your mission is to find the Treasure.")
        print("You are at cross road. where do you want to go?")
        choice = input("    Type \"left\" or \"right\"\n").lower()
        if choice == "left":
            print("You've come to a lake. There is an island in middle of lake.")
            choice = input("    Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n").lower()
            if choice == "wait":
                print("You reached safely.")
                choice = input("There are three doors \"Red\" , \"Blue\", \"Green\" Which door will you choose?\n").lower()
                if choice == "blue":
                    print("You Win !!")
                else:
                    print("Game Over.")
            else:
                print("Game Over. You were eaten by Sharks.")
        else:
            print("Game Over. You fell in pit of poisonous venom.")    
    else:
        print("\nGoodbye, adventurer.\n")
