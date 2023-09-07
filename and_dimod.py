from dimod.generators import and_gate
from dimod import ExactSolver
import numpy as np

'''
bqm = and_gate('a', 'b', 'c')


sampler = ExactSolver()
sampleset = sampler.sample(bqm)
print(sampleset)
print(bqm)
'''


bqm = [[0,1,-2],[0,0,-2],[0,0,3]]

sampler = ExactSolver()
sampleset = sampler.sample_qubo(bqm)
print(sampleset)


print(bqm)