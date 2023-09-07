from dimod.generators import and_gate
from dimod import ExactSolver
import numpy as np

bqm = and_gate('a', 'b', 'c')

#bqm = ({'a': 0.0, 'b': 0.0, 'c': 3.0}, {('b', 'a'): 1.0, ('c', 'a'): -2.0, ('c', 'b'): -2.0}, 0.0, 'BINARY')


sampler = ExactSolver()
sampleset = sampler.sample(bqm)
print(sampleset)
print(bqm)