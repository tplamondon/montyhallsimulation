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
            door = x
    return door, (0+1+2)-(goat+choiceDoor)

def simulate():
    """
    Simulate one thing
    """
    doors = getRandomDoorArray()
    pickedDoor = chooseDoor()
    goatDoor, switchDoor = openGoatDoor(pickedDoor, doors)
    return doors[goatDoor], doors[switchDoor]


def main():
    sumFirstChoice = 0
    sumSwitchChoice = 0
    #simulate
    choiceDoorBool, switchDoorBool = simulate()



if __name__ == "__main__":
    main()
