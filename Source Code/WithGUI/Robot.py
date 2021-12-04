# Author : Ammar Abu Shamleh

# This class defines the Robot object, which contains data about the robot's position, points, number of moves taken, and strategy

import random


class Robot(object):
    x = 0  # x coordinate of robot in room
    y = 0  # y coordinte of robot in room
    points = 0  # Number of points robot has accrued (can be negative)
    moves = 0  # Number of moves robot has made since creation

    strategy = [0 for x in
                range(243)]  # The strategy used by the robot. Elements represent actions for specific situations

    def __init__(self):
        # self.x = random.randint(0,9)
        # self.y = random.randint(0,9)
        self.x = 0
        self.y = 0
        self.points = 0
        self.moves = 0

    def moveRobot(self, newX, newY):
        # Move robot to new coordinate
        self.x = newX
        self.y = newY

    def makeAction(self, act, room):
        # Given an action number and the room object to act on, perform the specfied action
        if act == 0:
            # Move north
            if room.isWall(self.x, self.y - 1):
                # Hit a wall. Subtract 5 points
                self.points -= 5
            else:
                # Moved north
                self.y -= 1
            # Increment number of moves
            self.moves += 1

        elif act == 1:
            # Move south
            if room.isWall(self.x, self.y + 1):
                # Hit a wall. Subtract 5 points
                self.points -= 5
            else:
                # Moved south
                self.y += 1
            # Increment number of moves
            self.moves += 1

        elif act == 2:
            # Move east
            if room.isWall(self.x + 1, self.y):
                # Hit a wall. Subtract 5 points
                self.points -= 5
            else:
                # Moved south
                self.x += 1
            # Increment number of moves
            self.moves += 1

        elif act == 3:
            # Move west
            if room.isWall(self.x - 1, self.y):
                # Hit a wall. Subtract 5 points
                self.points -= 5
            else:
                # Moved west
                self.x -= 1
            # Increment number of moves
            self.moves += 1

        elif act == 4:
            # Do nothing
            self.moves += 1

        elif act == 5:
            # Attempt to pick up can
            if room.pickUpCan(self.x, self.y):
                # Picked up can. Add 10 points
                self.points += 10
            else:
                # No can in current tile. Subtract 1 point
                self.points -= 1
            # Increment number of moves
            self.moves += 1

        else:
            # Take random action
            # TODO: Should add error checking to catch action numbers not in (0-6)
            self.makeAction(random.randint(0, 5), room)

    def changeStrat(self, newStrat):
        # Given a strategy, make that this robot object's new strategy for acting in response to situations
        self.strategy = newStrat

    def decide(self, room, situations):
        # Given the list of situation mappings, and a room, decide on a course of action using current strategy
        sit = room.findSituation(self.x, self.y, situations)  # Find situation number
        action = self.strategy[sit]  # Find strategy using situation number
        self.makeAction(action, room)  # Perform action
        return action  # Return a number describing the action taken (i.e. 0 means attempted to move north)
