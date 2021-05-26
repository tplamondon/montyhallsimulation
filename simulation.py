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
    door = -1
    for x in range(len(doors)):
        if doors[x] == False and x != choiceDoor:
            door = x
    return door

def simulate():
    """
    Simulate one thing
    """
    print("Getting random door")
    doors = getRandomDoorArray()
    pickedDoor = chooseDoor()


def main():
    print("Start of Simulation")


if __name__ == "__main__":
    main()
