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

    f = open('parentselection.csv', 'a')
    f.write(time.strftime("START_%Y-%m-%d_%H:%M\n"))
    f.write('K\tGen\tBest Points\n')

    for k in range(1, 51):
        GAConstants.k = k

        def gen_callback(i, fitnesses, curGen, nextGen, bestCurCandidate):
            print('{}\t{}\t{}'.format(k, i, fitnesses[bestCurCandidate]))
            f.write('{}\t{}\t{}\n'.format(k, i, fitnesses[bestCurCandidate]))

        GAConstants.generation_callback = gen_callback

        solution = GeneticAlgorithm.naturalSelection(1001)
        f.flush()
    f.close()
