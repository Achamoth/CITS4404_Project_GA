# Author : Ammar Abu Shamleh

import Robot
import Room
import random
from datetime import datetime

situations = {};

def setSituations(sitFromRunner):
    global situations;
    situations = sitFromRunner

def genInitialPopulation():
    #Generate the initial population of solution candidates randomly
    popSize = 150
    population = [[random.randint(0,6) for x in range(243)] for y in range(popSize)]
    return population

def checkFitness(individual):
    #Given an individual, check its fitness and return the value
    sum = 0 #sum of all points accrued over all simulations using strategy
    numMoves = 200 #Number of moves to simulate
    numSimulations = 10 #Number of simulations per individual

    #Run simulations using the strategy (individual)
    for i in range(numSimulations):

        #Create new robot and room
        robot = Robot.Robot()
        room = Room.Room()

        #Assign strategy to robot
        robot.changeStrat(individual)

        #Run 200 moves
        for j in range(numMoves):
            robot.decide(room, situations)

        #Add points to cumulative tally
        sum += robot.points;

    #Find average number of points for simulations
    avg = sum / numSimulations;

    #Return the average as a fitness score for the individual
    return avg;

def naturalSelection(numGens):
    #This function uses a genetic algorithm to find a good solution over the specified number of generations

    #Seed random number generator
    random.seed(datetime.now())

    #First, generate population of initial candidate solutions
    curGen = genInitialPopulation()

    #Now, perform the following steps for 1000 generations
    for i in range(numGens):

        #Mate pairs of individuals probabalistically based on fitnesses to produce offspring
        nextGen = mateParents(curGen)

        #Give each child a chance to mutate
        randomlyMutate(nextGen)

        #Print the best candidate's fitness from the current gen
        bestCurCandidate = findBestCandidate(curGen)
        print str(i) + ' : ' + str(checkFitness(bestCurCandidate))
        # print str(bestCurCandidate)

        #Make the current generation the next generation (i.e. move to the next generation and repeat)
        curGen = nextGen

    #In the last generation, find the individual with the highest fitness
    bestCandidate = findBestCandidate(curGen)

    #Return the best candidate as the final solution
    return bestCandidate

def findAllFitnesses(population):
    #Given a population of individuals (array), return an array containing all fitnesses, with consistent index positioning

    #Create empty array of fitnesses
    fitnesses = [0 for x in range(len(population))]

    #For each individual, find its fitness, and store it in the array
    j=0
    for i in range(len(population)):
        curFitness = checkFitness(population[i])
        fitnesses[j] = curFitness
        j += 1

    #Return array of fitnesses
    return fitnesses

def mateParents(population):
    #Given a population of solution candidates, and an array of their fitnesses, probabalistically mate parents and produce offspring
    #Return populiation of offspring (as array of solution candidates), of same size as initial population

    #Find size of population
    initPopSize = len(population)

    #Create empty child population
    offspring = [[0 for y in range(243)] for x in range(initPopSize)]

    #Probabalistically mate parents based on fitness until a full population of offspring is produced. Use 10-way tournament selection
    numOffspring = 0
    while(numOffspring < initPopSize):
        parents = []
        parents.append(findParent(population, initPopSize))
        parents.append(findParent(population, initPopSize))
        curOffspring = getChildren(parents)
        offspring[numOffspring] = curOffspring[0]
        offspring[numOffspring+1] = curOffspring[1]
        #TODO: Can add in a check for fitness on offspring here to determine whether or not to add them
        numOffspring += 2

    #Return population of offspring
    return offspring

def findParent(population, popSize):
    #Find parent for generating offspring using k-way tournament selection
    #TODO: Experiment with different values of k
    best = []
    bestFitness = -20000
    k = 5 #5-way tournament selection
    for i in range(k):
        ind = population[random.randint(0,popSize-1)]
        curFitness = checkFitness(ind)
        if(curFitness > bestFitness):
            best = ind
            bestFitness = curFitness
    return best

def getChildren(parents):
    #Given a pair of parents, generate and return two children
    #TODO: Experiment with different variants of this function
    children = []
    splicePoint = random.randint(100,180)
    #Get 0-slicePoint chunk from first parent
    parent1FirstChunk = (parents[0])[0:splicePoint]
    #Get slicePoint-242 chunk from first parent
    parent1SecondChunk = (parents[0])[splicePoint:len(parents[0])]
    #Get 0-slicePoint chunk from second parent
    parent2FirstChunk = (parents[1])[0:splicePoint]
    #Get slicePoint-242 chunk from second parent
    parent2SecondChunk = (parents[1])[splicePoint:len(parents[1])]

    #Create children
    child1 = parent1FirstChunk + parent2SecondChunk
    child2 = parent2FirstChunk + parent1SecondChunk
    children.append(child1)
    children.append(child2)

    #Return children
    return children

def randomlyMutate(population):
    #Given a population of individuals, randomly mutate the individuals

    #Loop over all individuals
    for individual in population:
        #Each individual has a 1/12 chance of mutating
        if(random.randint(1,12) == 1):
            #Mutate the individual. Choose two random points in the individual's genome, and mutate all cells between them
            start = random.randint(0,121)
            end = random.randint(122,242)
            for i in range(start, end):
                #Randomize this element of the genome
                individual[i] = random.randint(0,6)
        else:
            #Don't mutate the individual
            continue

def findBestCandidate(population):
    #Given a population, return the individual with the highest fitness
    bestFitness = -1000
    bestCandidate = []
    for individual in population:
        curFitness = checkFitness(individual)
        if (curFitness >= bestFitness):
            bestFitness = curFitness
            bestCandidate = individual
    #Return best candidate
    return bestCandidate
