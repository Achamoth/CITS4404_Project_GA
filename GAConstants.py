# Tournament Selection K value
k = 15 # Default value of k

def empty_generation_callback(i, fitnesses, curGen, nextGen, bestCurCandidate):
    pass

# Print callback at the end of a generation
# i, fitnesses, curGen, nextGen, bestCurCandidate => None
generation_callback = empty_generation_callback

# Select a parent
# population, popSize, fitnesses => selected_parent
findParent = None

