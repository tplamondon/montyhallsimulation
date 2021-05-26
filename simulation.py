
import random

def getRandomDoorArray():
    doors = [False, False, False]
    car = random.randrange(3)
    doors[car] = True
    return doors


def simulate():
    print("Getting random door")
    doors = getRandomDoorArray()

def main():
    print("Start of Simulation")


if __name__ == "__main__":
    main()
