# Author : Ammar Abu Shamleh, Modified by Zen Ly
import time

import FileOps
import GAConstants
import GeneticAlgorithm
import Robot
import Room


# canAvg, avg, cansPickedUpAvg
# From Ammar's Runner.py
def testSolution(solution):
    sum = 0
    canSum = 0
    cansPickedUpSum = 0
    for i in range(100):
        # Generate new room and robot
        robot = Robot.Robot()
        room = Room.Room()
        cansBefore = room.getNumCans()
        canSum += room.getNumCans()
        # Assign best solution to robot as its strategy
        robot.changeStrat(solution)
        for j in range(200):
            # Run 200 actions using strategy
            robot.decide(room, situations)
        # Add number of points to cumulative sum
        sum += robot.points
        # Check how many cans were picked up
        cansPickedUp = cansBefore - room.getNumCans()
        cansPickedUpSum += cansPickedUp
    # Find average
    avg = sum / 100
    canAvg = canSum / 100
    cansPickedUpAvg = cansPickedUpSum / 100

    # Print average
    # print 'Average Cans: ' + str(canAvg)
    # print 'Average Points: ' + str(avg)
    # print 'Average Number of Cans Picked Up: ' + str(cansPickedUpAvg)
    # print 'Strategy: ' + str(solution)
    return canAvg, avg, cansPickedUpAvg


if __name__ == '__main__':
    # Read in list of situation mappings from "Situationts.txt" file
    situations = FileOps.readSituations('Situations.txt')

    # Set situations for genetic algorithm
    GeneticAlgorithm.setSituations(situations)

    f = open('parentselection.csv', 'a')


    def printBoth(val):
        print(str(val))
        f.write(str(val) + '\n')


    printBoth(time.strftime("START_%Y-%m-%d_%H:%M"))
    printBoth('K\tGeneration\tBest Fitness\tCan Average\tPoint Avg\tCans Picked Up Average')

    # test_list = range(1, 51)
    test_list = [2, 3, 5, 10, 15, 20, 50, 100, 150, 200]

    for k in test_list:
        for r in range(1, 6):
            GAConstants.k = k

            generations = 1001  # So that 1000 gets printed


            def gen_callback(i, fitnesses, curGen, nextGen, bestCurCandidate):
                canAvg, avg, cansPickedUpAvg = testSolution(curGen[bestCurCandidate])
                printBoth(
                    '{}\t{}\t{}\t{}\t{}\t{}'.format(str(k) + '_' + str(r), i, fitnesses[bestCurCandidate], canAvg, avg,
                                                    cansPickedUpAvg))
                f.flush()


            GAConstants.generation_callback = gen_callback

            solution = GeneticAlgorithm.naturalSelection(generations)
            f.flush()
    f.flush()
    f.close()
