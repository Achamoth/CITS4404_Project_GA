# Author : Ammar Abu Shamleh

import Room
import Robot
import FileOps
import GeneticAlgorithm

#Read in list of situation mappings from "Situationts.txt" file
situations = FileOps.readSituations('Situations.txt')

#Set situations for genetic algorithm
GeneticAlgorithm.setSituations(situations)

#Find best solution over 1000 generations
solution = GeneticAlgorithm.naturalSelection(1000)

#Test solution by running it on 200 actions with a robot in a random room, 100 times over, and finding average number of points
sum = 0
for i in range(100):
    #Generate new room and robot
    robot = Robot.Robot()
    room = Room.Room()
    #Assign best solution to robot as its strategy
    robot.changeStrat(solution)
    for j in range(200):
        #Run 200 actions using strategy
        robot.decide(room, situations)
    #Add number of points to cumulative sum
    sum += robot.points
#Find average
avg = sum / 100

#Print average
print 'Average Points: ' + str(avg)
print 'Strategy: ' + str(solution)
