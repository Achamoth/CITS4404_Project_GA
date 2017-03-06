# Author : Ammar Abu Shamleh

import Robot
import Room
import random

situations = {};

def setSituations(sitFromRunner):
    global situations;
    situations = sitFromRunner

def genInitialPopulation():
    #Generate the initial population of solution candidates randomly
    population = [[random.randint(0,6) for x in range(243)] for y in range(200)]
    return population

def checkFitness(individual):
    #Given an individual, check its fitness and return the value
    sum = 0 #sum of all points accrued over 100 simulations using strategy

    #Run 100 simulations using the strategy (individual)
    for i in Range(100):

        #Create new robot and room
        robot = Robot.Robot()
        room = Room.Room()

        #Assign strategy to robot
        robot.changeStrat(individual)

        #Run 200 moves
        for j in Range(200):
            robot.decide(room, Runner.situations)

        #Add points to cumulative tally
        sum += robot.points;

    #Find average number of points for simulations
    avg = sum / 200;

    #Return the average as a fitness score for the individual
    return avg;

def naturalSelection(numGens):
    #This function uses a genetic algorithm to find a good solution over the specified number of generations

    #First, generate population of initial candidate solutions
    initPop = genInitialPopulation()
    curGen = initPop

    #Now, perform the following steps for 1000 generations
    for i in Range(1000):
        #Check the fitness of each individual in the current population
        fitnesses = findAllFitnesses(curGen)

        #Mate pairs of individuals probabalistically based on fitnesses to produce offspring
        nextGen = mateParents(curGen, fitnesses)

        #Give each child a chance to mutate
        randomlyMutate(nextGen)

        #Make the current generation the next generation (i.e. move to the next generation and repeat)
        curGen = nextGen

    #In the last generation, find the individual with the highest fitness
    bestCandidate = findBestCandidate(curGen)

    #Return the best candidate as the final solution
    return bestCandidate

def findAllFitnesses(population):
    #Given a population of individuals (array), return an array containing all fitnesses, with consistent index positioning

    #Create empty array of fitnesses
    fitnesses = [0 for x in Range(len(population))]

    #For each individual, find its fitness, and store it in the array
    j=0
    for i in Range(len(population)):
        curFitness = checkFitness(population[i])
        fitnesses[j] = curFitness
        j += 1

    #Return array of fitnesses
    return fitnesses

def mateParents(population, fitnesses):
    #Given a population of solution candidates, and an array of their fitnesses, probabalistically mate parents and produce offspring
    #Return populiation of offspring (as array of solution candidates), of same size as initial population

    #Find size of population
    initPopSize = len(populiation)

    #Create population of empty offspring
    offspring = [0 for y in Range(200)]

    #Probabalistically mate parents based on fitness until a full population of offspring is produced
    #TODO: Complete

    #Return population of offspring
    return offspring

def randomlyMutate(population):
    #Given a population of individuals, randomly mutate the individuals

    #Loop over all individuals
    for individual in population:
        #Each individual has a 10% chance of mutating
        if(random.randint(1,10) == 1):
            #Mutate the individual. Choose two random points in the individual's genome, and mutate all cells between them
            start = random.randint(0,121)
            end = random.randint(122,242)
            for i in Range(start, end):
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
