# Author : Ammar Abu Shamleh

# This module deals with any File I/O that needs to take place

# This function reads in the specified file, and returns a dictionary of situation mappings
def readSituations(fileName):
    #Open file
    fin = open(fileName, 'r')
    situations = {} #Create dictionary
    fin.readline() #Skip first line (header)
    #Read all lines in file
    for eachLine in fin:
        #Split current line around comma delimiter
        tokens = eachLine.split(',')
        for token in tokens:
            #Strip all tokens found by splitting line (i.e. remove leading and trailing whitespace)
            token.strip()

        #Find encodings for north, south, east, west, and current tiles (i.e. Empty tile = 0, Can = 1, Wall = 2)
        numNorth = tileToNum(tokens[0])
        numSouth = tileToNum(tokens[1])
        numEast = tileToNum(tokens[2])
        numWest = tileToNum(tokens[3])
        numCurrent = tileToNum(tokens[4])
        sitNum = int(tokens[5]) #This is the 'situation' number for this specific combination of tile circumstances
        key = str(numNorth) + str(numSouth) + str(numEast) + str(numWest) + str(numCurrent) #Encode situation as a string (for use as key in dictionary)
        situations[key] = sitNum #Store key-value pair in dictionary

    fin.close() #Close file
    #Return dictionary
    return situations


def tileToNum(tile):
    #Given a string describing a tile, return a number representing that tile's encoding
    if tile == 'Empty':
        #Empty tile
        return 0
    elif tile == 'Can':
        #Tile has a can
        return 1
    elif tile == 'Wall':
        #Tile is a wall
        return 2
    else:
        #TODO: Should throw an error (invalid tile description)
        return 0
