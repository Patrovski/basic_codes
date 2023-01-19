
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
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

first_choice = input("You\'re at a crossroad and found two paths. Left or right? ").lower()

if first_choice == "left":
  second_choice = input('You see an island in the distant sea.\n Do you want to "swim" or "wait" for a boat? ').lower()
  if second_choice == "wait":
    third_choice = input("You have arrived at the island unharmed but now found a house with 3 doors. Which door will you enter?\n red, blue, yellow or green? ").lower()
    if third_choice == "yellow":
      print("You have found the treasure... it was inside you all along. Gg.")
    elif third_choice == "blue":
      print("You have entered a room full of other rival pirates. You got killed.")
    elif third_choice == "red":
      print("You entered a boobytrapped room with a sawn-off shotgun.\n You died in agony.")
    else:
      print("You just entered a pit and got inpaled on a floor of spikes. Fatality")
  else:
    print("You got surrounded by sharks and they tore you to pieces. Game over")
else:
  print("You met a band of cannibals. They skinned you alive and ate you. Game over")

