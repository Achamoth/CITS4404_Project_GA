#Author: Ammar Abu Shamleh
import Room
import Robot

#Constants for describing a square's state
EMPTY = 0
CAN = 1
WALL = 2

#Constants for describing the robot's action
MOVE_NORTH = 0
MOVE_SOUTH = 1
MOVE_EAST = 2
MOVE_WEST = 3
DO_NOTHING = 4
PICK_UP_CAN = 5
RANDOM = 6

def getSolution(situations):
    #Create empty solution
    solution = [0 for x in range(243)]

    #Loop over all situations
    for key in situations.keys():
        #Examine situation and decide on action
        north = int(key[0])
        south = int(key[1])
        east = int(key[2])
        west = int(key[3])
        current = int(key[4])

        #Prioritise picking up can in current square
        if(current == CAN):
            solution[situations[key]] = PICK_UP_CAN
        else:
            solution[situations[key]] = RANDOM

    #Return solution
    return solution
