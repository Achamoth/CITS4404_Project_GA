# Author: Ammar Abu Shamleh
import FileOps

# Constants for describing a square's state
EMPTY = 0
CAN = 1
WALL = 2

# Constants for describing the robot's action
MOVE_NORTH = 0
MOVE_SOUTH = 1
MOVE_EAST = 2
MOVE_WEST = 3
DO_NOTHING = 4
PICK_UP_CAN = 5
RANDOM = 6


def getSolution(situations):
    # Create empty solution
    solution = [0 for x in range(243)]

    # Loop over all situations
    for key in situations.keys():
        # Examine situation and decide on action
        north = int(key[0])
        south = int(key[1])
        east = int(key[2])
        west = int(key[3])
        current = int(key[4])

        # Prioritise picking up can in current square
        if (current == CAN):
            solution[situations[key]] = PICK_UP_CAN
        else:
            solution[situations[key]] = RANDOM

    # Return solution
    return solution


def zen(north, south, east, west, current):
    if current == CAN:
        if north == CAN:
            return MOVE_NORTH
        elif west == CAN:
            return MOVE_WEST
        else:
            return PICK_UP_CAN

    if north == CAN:
        return MOVE_NORTH
    if south == CAN:
        return MOVE_SOUTH
    if east == CAN:
        return MOVE_EAST
    if west == CAN:
        return MOVE_WEST

    if south == WALL:
        return MOVE_EAST if not east == WALL else MOVE_NORTH
    if east == WALL:
        return MOVE_NORTH if not north == WALL else MOVE_WEST

    if north == WALL:
        return MOVE_WEST if not west == WALL else MOVE_SOUTH
    if west == WALL:
        return MOVE_EAST  # MOVE_SOUTH if not south == WALL else MOVE_EAST

    return RANDOM


def getSolutionFunc(func):
    # type: (Map[(int, int, int, int, int),int], Callable[[int, int, int, int, int], int]) -> List[int]
    """Generates Solution List from a function that given the
    (north, south, east, west, current) squares returns an action"""
    situations = FileOps.readSituations('Situations.txt')

    # Create empty solution
    solution = [0 for x in range(243)]

    # Loop over all situations
    for key in situations.keys():
        north = int(key[0])
        south = int(key[1])
        east = int(key[2])
        west = int(key[3])
        current = int(key[4])
        solution[situations[key]] = func(north, south, east, west, current)

    return solution
