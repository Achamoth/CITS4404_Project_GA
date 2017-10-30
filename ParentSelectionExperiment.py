# Author : Ammar Abu Shamleh, Modified by Zen Ly
import Room
import Robot
import FileOps
import GeneticAlgorithm
import GAConstants
import time

if __name__ == '__main__':
    # Read in list of situation mappings from "Situationts.txt" file
    situations = FileOps.readSituations('Situations.txt')

    # Set situations for genetic algorithm
    GeneticAlgorithm.setSituations(situations)

    bestK = -1
    bestKPoints = 0
    f = open('parentselection.csv', 'a')
    f.write(time.strftime("START_%Y-%m-%d_%H:%M\n"))
    f.write('K\tCans\tPoints\tStrategy\n')

    for k in range(1, 51):
        GAConstants.setK(k)

        # Find best solution over 1000 generations
        solution = GeneticAlgorithm.naturalSelection(1000)

        # Test solution by running it on 200 actions with a robot in a random room,100 times over,and finding average number of points
        sum = 0
        canSum = 0
        for i in range(100):
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
        avg = sum / 100
        canAvg = canSum / 100

        # Update Best
        if avg > bestKPoints:
            bestK = k
            bestKPoints = avg

        # Log Result
        print('{}\t{}\t{}\t{}\n'.format(k, canAvg, avg, solution))
        f.write('{}\t{}\t{}\t{}\n'.format(k, canAvg, avg, solution))

    f.close()
