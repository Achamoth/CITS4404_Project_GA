# Author : Ammar Abu Shamleh

import random
import sys


class Room(object):

    #2d array (10 by 10). 1 in any tile with a can, 0 in any empty tile
    def __init__(self, width=10, height=10, chance=0.5):
        self.width = width
        self.height = height
        self.cans = [[0 for _ in range(width)] for _ in range(height)]
        self.numCans = 0
        for j in range(0, height):
            for i in range(0, width):
                if random.random() < chance:
                    self.cans[j][i] = 1
                    self.numCans += 1

    def pickUpCan(self, x, y):
        #If the specified coordinate has a can, remove it, and return true. Otherwise, return false
        if self.cans[y][x] == 1:
            self.cans[y][x] = 0
            self.numCans -= 1
            return True
        else:
            return False

    def isWall(self, x, y):
        #If the specified coordinate is out of bounds (i.e. beyond a wall, or is a wall), return true. Otherwise return false
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            #Coordinate is a wall (or out of bounds)
            return True
        else:
            return False

    def findSituation(self, x, y, situations):
        #Given a coordinate tuple, and a dictionary of situation mappings, return the number that describes the specific situation as seen at the specified coordinate
        #i.e. (If the current tile and all adjacent tiles are empty, that is situation 0)
        #Get encodings for each adjacent tile and the current tile (Empty = 0, Can = 1, Wall = 2)
        north = self.getEncoding(x, y - 1)
        south = self.getEncoding(x, y + 1)
        east = self.getEncoding(x + 1, y)
        west = self.getEncoding(x - 1, y)
        current = self.getEncoding(x, y)
        #Construct key for situation (based on current tile and adjacent tiles)
        key = str(north) + str(south) + str(east) + str(west) + str(current)
        #Find situation number from dictionary
        sit = situations[key]
        #Return situation number
        return sit

    def getEncoding(self, x, y):
        #Given a coordinate tuple, return an encoding describing that tile (i.e. empty = 0, can = 1, wall = 2)
        if self.isWall(x, y):
            return 2
        elif self.cans[y][x] == 1:
            return 1
        else:
            return 0

    def getNumCans(self):
        #Return the number of cans present in the room
        return self.numCans

    def printRoom(self):
        #Print the room as a string
        for y in range(self.height):
            for x in range(self.width):
                if(self.cans[y][x] == 1):
                    sys.stdout.write('C ')
                else:
                    sys.stdout.write('E ')
                sys.stdout.flush()
            sys.stdout.write('\n')
            sys.stdout.flush()

    def isCan(self, x, y):
        return not self.isWall(x, y) and self.cans[y][x] == 1