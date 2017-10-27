import Runner
import GeneticAlgorithm
import sys

tests = ["OneSplit", "TwoSplits", "ThreeSplits", "FourSplits", "FiveSplits", "SixSplits", "SevenSplits", "EightSplits", "NineSplits", "TenSplits"]
for i in range(len(tests)):
    for j in range(1,6): # 5 iterations
        filename = "Terminal Outputs/test" + tests[i] + str(j) + ".txt"
        sys.stdout = open(filename, 'w')
        Runner.runSimulation(1, i+1)
        sys.stdout = sys.__stdout__
        print 'Completed ' + filename

"""
parent1 = [x for x in range(243)]
parent2 = [-x for x in range(243)]
GeneticAlgorithm.getChildren([parent1, parent2], 2)
"""
