# Author : Zen Ly
import random
import time

import FileOps
import GAConstants
import GeneticAlgorithm
import ParentSelectionExperiment

if __name__ == '__main__':
    situations = FileOps.readSituations('Situations.txt')
    GeneticAlgorithm.setSituations(situations)

    f = open('parentselectionother.csv', 'a')


    def printBoth(val):
        print(str(val))
        f.write(str(val) + '\n')


    printBoth(time.strftime("START_%Y-%m-%d_%H:%M"))
    printBoth('Function\tGeneration\tBest Fitness\tCan Average\tPoint Avg\tCans Picked Up Average')


    def random_sel(population, popSize, fitnesses):
        return population[random.randint(0, popSize - 1)]


    # Negative fitness is treated as zero
    # If total fitness is zero, randomly selects a parent
    def roulette_wheel(population, popSize, fitnesses):
        total_fitness = 0
        for fitness in fitnesses:
            total_fitness += max(0, fitness)
        if total_fitness <= 0:
            return random_sel(population, popSize, fitness)
        target_fitness = random.random() * total_fitness
        current_fitness = 0
        for ind in range(0, popSize):
            current_fitness += max(0, fitnesses[ind])
            if current_fitness < target_fitness:
                continue
            return population[ind]
        raise


    #
    # def truncation_half(population, popSize, fitnesses):
    #    # Find


    # From Ammar's GeneticAlgorithm.py
    def tournament_k15(population, popSize, fitnesses):
        best = population[0]
        bestFitness = fitnesses[0]
        k = 15
        for i in range(k):
            curRand = random.randint(0, popSize - 1)
            ind = population[curRand]
            curFitness = fitnesses[curRand]
            if (curFitness > bestFitness):
                best = ind
                bestFitness = curFitness
        return best


    parent_selection_functions = [roulette_wheel, random_sel, tournament_k15]

    for parent_selection_func in parent_selection_functions:
        GAConstants.findParent = parent_selection_func

        generations = 4001  # So that 1000 gets printed


        def gen_callback(i, fitnesses, curGen, nextGen, bestCurCandidate):
            canAvg, avg, cansPickedUpAvg = ParentSelectionExperiment.testSolution(situations, curGen[bestCurCandidate])
            printBoth('{}\t{}\t{}\t{}\t{}\t{}'.format(parent_selection_func.__name__
                                                      , i, fitnesses[bestCurCandidate], canAvg, avg, cansPickedUpAvg))
            f.flush()


        GAConstants.generation_callback = gen_callback

        solution = GeneticAlgorithm.naturalSelection(generations)
        f.flush()
    printBoth(time.strftime("FINISHED_%Y-%m-%d_%H:%M"))
    f.flush()
    f.close()
