# Author : Ammar Abu Shamleh
from timeit import default_timer

import FileOps
import GeneticAlgorithm
import Robot
import Room


def runSimulation(numGens=6000, numSplices=2):
    # Read in list of situation mappings from "Situationts.txt" file
    situations = FileOps.readSituations('Situations.txt')

    # Set situations for genetic algorithm
    GeneticAlgorithm.setSituations(situations)

    # Hand coded solution (tends to get about 150 points when run over 200 actions)
    # solution = [3,5,3,3,5,3,2,5,2,2,5,2,2,5,2,2,5,2,3,5,3,3,5,3,1,5,1,1,5,1,1,5,1,1,5,1,2,5,2,2,5,2,2,5,2,1,5,1,1,5,1,1,5,1,3,5,3,3,5,3,2,5,2,2,5,2,2,5,2,2,5,2,3,5,3,3,5,3,0,5,0,0,5,0,0,5,0,0,5,0,0,5,0,0,5,0,0,5,0,0,5,0,0,5,0,0,5,0,0,5,0,0,5,0,0,5,0,0,5,0,0,5,0,0,5,0,0,5,0,0,5,0,0,5,0,0,5,0,0,5,0,0,5,0,0,5,0,0,5,0,0,5,0,0,5,0,0,5,0,0,5,0,3,5,3,3,5,3,2,5,2,2,5,2,2,5,2,2,5,2,3,5,3,3,5,3,1,5,1,1,5,1,1,5,1,1,5,1,1,5,1,1,5,1,1,5,1,1,5,1,1,5,1,1,5,1,3,5,3,3,5,3,2,5,2,2,5,2,2,5,2,2,5,2,3,5,3,3,5,3,5,5,5]

    # Melanie Mitchell's Solution
    # solution = [2,5,4,3,5,5,1,5,3,2,5,6,2,3,5,2,5,1,0,5,6,3,5,5,4,6,1,1,5,1,3,3,6,1,5,4,1,5,1,0,3,4,1,5,6,1,1,0,5,5,0,1,5,0,0,5,2,0,3,0,2,5,6,2,5,6,1,3,2,2,5,2,3,5,0,3,2,5,1,1,2,0,5,2,3,3,3,0,5,4,0,5,5,2,3,1,2,5,5,0,5,1,3,3,6,1,5,4,1,5,0,6,6,5,2,6,4,1,5,0,2,6,6,5,0,6,0,1,2,2,6,4,4,5,3,6,0,5,6,3,1,5,2,0,2,5,6,4,3,1,0,5,4,3,5,4,6,3,2,4,0,4,3,5,0,3,3,4,1,5,3,2,5,0,2,5,3,2,5,1,3,5,2,3,5,2,0,4,5,1,5,0,1,3,0,1,5,6,2,1,3,4,3,6,2,5,2,3,5,3,2,2,3,1,3,5,0,5,1,2,6,0,5,1,3,3,5,6,2,0,1,5,2,4,5,1,4,3,4,3,4,3,2]

    # Zen's Solution
    # solution = HandCoded.getSolutionFunc(HandCoded.zen)

    # Hand coded solution
    # solution = HandCoded.getSolution(situations)

    # GA 3000 Gens (40 cans roughly) solution
    # solution = [1,5,4,3,5,5,0,5,4,2,2,0,3,2,4,6,2,4,0,3,5,3,4,6,0,6,5,1,5,6,3,5,0,1,5,4,2,2,5,3,2,3,4,2,6,1,6,0,4,0,4,2,0,5,2,6,2,6,4,5,1,6,4,6,5,4,6,2,2,5,6,1,0,0,5,4,6,6,2,6,1,6,0,4,1,0,5,0,5,0,1,0,1,0,0,3,1,0,0,5,4,0,0,5,3,4,1,4,5,0,3,1,0,5,0,5,0,3,0,6,5,0,2,2,6,0,5,3,4,6,1,0,2,3,6,0,4,3,1,1,1,1,2,5,2,6,0,0,2,4,1,4,2,5,1,0,2,0,4,1,6,3,1,5,0,3,3,2,2,5,2,1,5,5,6,3,3,2,5,3,3,6,5,3,1,3,2,4,5,1,5,1,1,3,2,1,5,0,2,5,5,3,6,3,1,5,6,2,1,2,1,0,3,2,1,3,1,5,1,2,2,1,3,5,0,6,4,2,3,2,2,2,5,3,4,0,4,0,0,4,3,3,2]

    # GA 10000 Gens (50 cans). Best solution this GA has found
    solution = [1, 5, 4, 3, 5, 5, 2, 5, 3, 2, 2, 1, 3, 2, 3, 2, 5, 6, 0, 5, 1, 3, 5, 2, 1, 1, 6, 6, 5, 2, 3, 1, 1, 1, 5,
                1, 2, 1, 6, 3, 2, 0, 2, 5, 4, 3, 5, 0, 3, 5, 1, 0, 5, 5, 2, 5, 5, 2, 2, 3, 1, 2, 6, 2, 5, 4, 2, 3, 0, 2,
                5, 4, 0, 5, 6, 3, 2, 1, 0, 2, 1, 0, 5, 4, 0, 5, 2, 2, 0, 0, 2, 2, 4, 2, 2, 6, 3, 6, 4, 0, 5, 6, 3, 0, 6,
                2, 5, 6, 0, 1, 1, 6, 1, 0, 1, 5, 0, 0, 1, 4, 3, 2, 3, 3, 1, 2, 0, 5, 5, 3, 5, 5, 2, 3, 6, 0, 5, 0, 2, 3,
                5, 0, 5, 4, 0, 5, 5, 3, 3, 5, 2, 5, 6, 0, 5, 3, 1, 2, 3, 1, 3, 3, 1, 5, 4, 3, 5, 4, 2, 5, 4, 6, 2, 4, 1,
                2, 4, 2, 5, 6, 3, 5, 6, 3, 5, 3, 1, 4, 5, 1, 5, 6, 1, 1, 3, 1, 5, 4, 1, 2, 6, 0, 2, 5, 2, 5, 5, 1, 5, 0,
                6, 6, 5, 5, 4, 5, 3, 4, 6, 1, 5, 6, 0, 6, 4, 2, 2, 6, 5, 0, 1, 3, 0, 6, 6, 0, 4, 4, 5, 4, 5, 6, 1]

    # Find best solution over 1000 generations
    startTime = default_timer()
    # solution = GeneticAlgorithm.naturalSelection(numGens, numSplices)
    endTime = default_timer()

    # Test solution by running it on 200 actions with a robot in a random room,100 times over,and finding average number of points
    sum = 0
    canSum = 0
    for i in range(50):
        # Generate new room and robot
        robot = Robot.Robot()
        room = Room.Room()
        canSum += room.getNumCans()
        # Assign best solution to robot as its strategy
        robot.changeStrat(solution)
        for j in range(200):
            # Run 200 actions using strategy
            robot.decide(room, situations)
        # Add number of points to cumulative sum
        sum += robot.points
    # Find average
    avg = sum / 50
    canAvg = canSum / 50

    # Print average
    # print 'Average Cans: ' + str(canAvg)
    # print 'Average Points: ' + str(avg)
    # print 'Execution Time: ' + str(endTime - startTime)
    # print 'Strategy: ' + str(solution)
    print 'Max Points: ' + str(canAvg * 10)
    print 'Avg Points: ' + str(avg)
    print 'Percentage: ' + str(100 * float(float(avg) / float(canAvg * 10)))


if __name__ == "__main__":
    runSimulation()
