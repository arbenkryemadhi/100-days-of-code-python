print('''
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
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island. Made by Arben KRYEMADHI!")
print("Your mission is to find the treasure.") 

crossroad_input = input("You are in front of a crossroad, do you go Left or Right? ").lower()
if crossroad_input == "right":    
    lake_input = input("You are standing in front of a lake do you Swim or Run (around)? ").lower()
    
    if lake_input == "swim":
        door_input = input("You were able to swim across the lake, now you are in front a house with three doors: red, blue, yellow. Which one do you chose? ").lower()
        
        if door_input == "blue":
            print("Congratulations! You found the treasure and won!")
        else:
            print("You went into the witch's house. Game Over!")
    else:
        print("You got attacked by a snake. Game Over!")
else:
    print("You fell into a hole. Game Over!")