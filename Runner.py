# Author : Ammar Abu Shamleh
import Room
import Robot
import FileOps
import GeneticAlgorithm

# Windows Threading support
if __name__ == '__main__':
    #Read in list of situation mappings from "Situationts.txt" file
    situations = FileOps.readSituations('Situations.txt')

    #Set situations for genetic algorithm
    GeneticAlgorithm.setSituations(situations)

    #Hand coded solution (tends to get about 150 points when run over 200 actions)
    #solution = [3,5,3,3,5,3,2,5,2,2,5,2,2,5,2,2,5,2,3,5,3,3,5,3,1,5,1,1,5,1,1,5,1,1,5,1,2,5,2,2,5,2,2,5,2,1,5,1,1,5,1,1,5,1,3,5,3,3,5,3,2,5,2,2,5,2,2,5,2,2,5,2,3,5,3,3,5,3,0,5,0,0,5,0,0,5,0,0,5,0,0,5,0,0,5,0,0,5,0,0,5,0,0,5,0,0,5,0,0,5,0,0,5,0,0,5,0,0,5,0,0,5,0,0,5,0,0,5,0,0,5,0,0,5,0,0,5,0,0,5,0,0,5,0,0,5,0,0,5,0,0,5,0,0,5,0,0,5,0,0,5,0,3,5,3,3,5,3,2,5,2,2,5,2,2,5,2,2,5,2,3,5,3,3,5,3,1,5,1,1,5,1,1,5,1,1,5,1,1,5,1,1,5,1,1,5,1,1,5,1,1,5,1,1,5,1,3,5,3,3,5,3,2,5,2,2,5,2,2,5,2,2,5,2,3,5,3,3,5,3,5,5,5]

    #Melanie Mitchell's Solution
    #solution = [2,5,4,3,5,5,1,5,3,2,5,6,2,3,5,2,5,1,0,5,6,3,5,5,4,6,1,1,5,1,3,3,6,1,5,4,1,5,1,0,3,4,1,5,6,1,1,0,5,5,0,1,5,0,0,5,2,0,3,0,2,5,6,2,5,6,1,3,2,2,5,2,3,5,0,3,2,5,1,1,2,0,5,2,3,3,3,0,5,4,0,5,5,2,3,1,2,5,5,0,5,1,3,3,6,1,5,4,1,5,0,6,6,5,2,6,4,1,5,0,2,6,6,5,0,6,0,1,2,2,6,4,4,5,3,6,0,5,6,3,1,5,2,0,2,5,6,4,3,1,0,5,4,3,5,4,6,3,2,4,0,4,3,5,0,3,3,4,1,5,3,2,5,0,2,5,3,2,5,1,3,5,2,3,5,2,0,4,5,1,5,0,1,3,0,1,5,6,2,1,3,4,3,6,2,5,2,3,5,3,2,2,3,1,3,5,0,5,1,2,6,0,5,1,3,3,5,6,2,0,1,5,2,4,5,1,4,3,4,3,4,3,2]

    #GA 3000 Gens (40 cans roughly) solution
    #solution = [1,5,4,3,5,5,0,5,4,2,2,0,3,2,4,6,2,4,0,3,5,3,4,6,0,6,5,1,5,6,3,5,0,1,5,4,2,2,5,3,2,3,4,2,6,1,6,0,4,0,4,2,0,5,2,6,2,6,4,5,1,6,4,6,5,4,6,2,2,5,6,1,0,0,5,4,6,6,2,6,1,6,0,4,1,0,5,0,5,0,1,0,1,0,0,3,1,0,0,5,4,0,0,5,3,4,1,4,5,0,3,1,0,5,0,5,0,3,0,6,5,0,2,2,6,0,5,3,4,6,1,0,2,3,6,0,4,3,1,1,1,1,2,5,2,6,0,0,2,4,1,4,2,5,1,0,2,0,4,1,6,3,1,5,0,3,3,2,2,5,2,1,5,5,6,3,3,2,5,3,3,6,5,3,1,3,2,4,5,1,5,1,1,3,2,1,5,0,2,5,5,3,6,3,1,5,6,2,1,2,1,0,3,2,1,3,1,5,1,2,2,1,3,5,0,6,4,2,3,2,2,2,5,3,4,0,4,0,0,4,3,3,2]

    #GA 10000 Gens (50 cans). Best solution this GA has found
    #solution = [1,5,4,3,5,5,2,5,3,2,2,1,3,2,3,2,5,6,0,5,1,3,5,2,1,1,6,6,5,2,3,1,1,1,5,1,2,1,6,3,2,0,2,5,4,3,5,0,3,5,1,0,5,5,2,5,5,2,2,3,1,2,6,2,5,4,2,3,0,2,5,4,0,5,6,3,2,1,0,2,1,0,5,4,0,5,2,2,0,0,2,2,4,2,2,6,3,6,4,0,5,6,3,0,6,2,5,6,0,1,1,6,1,0,1,5,0,0,1,4,3,2,3,3,1,2,0,5,5,3,5,5,2,3,6,0,5,0,2,3,5,0,5,4,0,5,5,3,3,5,2,5,6,0,5,3,1,2,3,1,3,3,1,5,4,3,5,4,2,5,4,6,2,4,1,2,4,2,5,6,3,5,6,3,5,3,1,4,5,1,5,6,1,1,3,1,5,4,1,2,6,0,2,5,2,5,5,1,5,0,6,6,5,5,4,5,3,4,6,1,5,6,0,6,4,2,2,6,5,0,1,3,0,6,6,0,4,4,5,4,5,6,1]

    #Find best solution over 1000 generations
    solution = GeneticAlgorithm.naturalSelection(10000)

    #Test solution by running it on 200 actions with a robot in a random room, 100 times over,and finding average number of points
    sum = 0
    canSum = 0
    for i in range(100):
        #Generate new room and robot
        robot = Robot.Robot()
        room = Room.Room()
        canSum += room.getNumCans()
        #Assign best solution to robot as its strategy
        robot.changeStrat(solution)
        for j in range(200):
            #Run 200 actions using strategy
            robot.decide(room,situations)
        #Add number of points to cumulative sum
        sum += robot.points
    #Find average
    avg = sum / 100
    canAvg = canSum/100

    #Print average
    print 'Average Cans: ' + str(canAvg)
    print 'Average Points: ' + str(avg)
    print 'Strategy: ' + str(solution)
