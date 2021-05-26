from typing import List
import random

def getRandomDoorArray():
    """
    Create a random door array
    """
    doors = [False, False, False]
    car = random.randrange(3)
    doors[car] = True
    return doors

def chooseDoor():
    """
    Choose a random door
    """
    return random.randrange(3)

def openGoatDoor(choiceDoor: int, doors: List[int]):
    """
    Choose the door to open that's not the choice
    """
    goat = -1
    for x in range(len(doors)):
        if doors[x] == False and x != choiceDoor:
            goat = x
    return goat, (0+1+2)-(goat+choiceDoor)

def simulate():
    """
    Simulate one thing
    """
    doors = getRandomDoorArray()
    pickedDoor = chooseDoor()
    goatDoor, switchDoor = openGoatDoor(pickedDoor, doors)
    return doors[pickedDoor], doors[switchDoor]


def main():
    TIMESTOSIMULATE = 100000
    sumFirstChoice = 0
    sumSwitchChoice = 0
    #simulate x times
    for x in range(TIMESTOSIMULATE):
        choiceDoorBool, switchDoorBool = simulate()
        if choiceDoorBool == True:
            sumFirstChoice += 1
        if switchDoorBool == True:
            sumSwitchChoice += 1
    percentSwitchWon = float(sumSwitchChoice) / float(TIMESTOSIMULATE)
    percentChoiceWon = float(sumFirstChoice) / float(TIMESTOSIMULATE)

    print(f"Keeping your first choice, you win {round(percentChoiceWon, 5)*100}% of the time")
    print(f"Switching your choice, you win {round(percentSwitchWon, 5)*100}% of the time")


if __name__ == "__main__":
    main()
