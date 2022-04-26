import random
import time

def main():
    print ("Chibong's Epic dice rolller")
    player_input = input("press d to roll the dice: ")
    if player_input.lower() == "d":
        dice_roller()
    elif player_input.lower() != "d":
        print("press d to roll the dice, please use your brain don't make me cry ")
        time.sleep(3)

def dice_roller():
    number = random.randint (1,6)
    if number == 1:
        print("you got a 1!")
        print ("you got the lowest number, better luck next time!")
        time.sleep(2)
        main()
    if number == 2:
        print("you got a 2!")
        time.sleep(2)
        main()
    if number == 3:
        print("you got a 3!")
        time.sleep(2)
        main()
    if number == 4:
        print("you got a 4!")
        time.sleep(2)
        main()
    if number == 5:
        print("you got a 5!")
        time.sleep(2)
        main()
    if number == 6:
        print("you got a 6!")
        print ("looks like u got the highest number in a dice, kudos to you")
        time.sleep(2)
        main()

main()