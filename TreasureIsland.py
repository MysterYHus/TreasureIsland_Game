print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
choice1 = input("You're at a crossroad, which way would you like to go? Type 'left' or 'right:\n").lower()

if choice1 == 'left':
    choice2 = input("You've come to a lake. There is an island in the middle of the lake. Type 'Wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
    if choice2 == 'wait':
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue.\nWhich door do you choose?\n").lower()
        if choice3 == 'red':
            print("You have found the treasure, you win!")
        elif choice3 == 'yellow':
            print("It's a room full of fire. You tripped, fell in, the door slammed shut and you burned to death. Game Over!")
        elif choice3 == 'blue':
            print("You enter a room full of beasts. They take their time eating you. You die a painful death. Game Over!")
        else:
            print("You chose a door that doesn't exist. Game Over!")
    else:
        print("You got killed by a stingray, Steve Irwin style. Game Over!")
else:
    print("You fell into a precipice. Game Over!")