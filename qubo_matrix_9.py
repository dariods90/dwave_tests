import numpy as np
from dimod import ExactSolver
from dwave.system import DWaveSampler, EmbeddingComposite
import dwave.inspector
import pandas as pd
pd.set_option("display.max_rows", 100000000)

# sampleset.first.sample takes the lowest energy sample result, without cutting any data

print("The correct string is unknown")


QUBO_ex15_lambda2 = np.array( [ [132, -90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -38, -120, 0, 0, -152, 0, 0, 0, 0, 0] ,
[0, 111, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -18, 0, 0, 0, 0, -120, 0, 0, 0, 0, -72, 0, 0, 0] ,
[0, 0, -32, -14, -14, 80, 42, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -60, 0, 0, -14, 0, 0, 0, 0, 0, 0, 0] ,
[0, 0, 0, -72, -14, 0, 42, 0, -60, 0, -60, 0, 0, 0, 0, 180, 0, 0, 0, 0, 0, 0, 0, -14, 0, 0, 0, 0, -60, 0, 0] ,
[0, 0, 0, 0, -159, 0, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 110, 176, 110, 0, 0, 0, 0, -14, 0, 0, 0, 0, 0, 88, 0] ,
[0, 0, 0, 0, 0, -161, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 250, 208, 0, 0, 0, 0, 0, 0, 0, 0, 0] ,
[0, 0, 0, 0, 0, 0, -64, -24, -24, 0, 0, 0, 0, 72, 0, 0, 0, 0, 0, 0, 0, 0, 0, 28, -24, 0, 0, 0, 0, 0, 0] ,
[0, 0, 0, 0, 0, 0, 0, -90, -24, 0, 0, 374, 0, 72, 0, 0, -170, 0, 0, -170, 0, 0, 0, 0, -24, 0, -136, 0, 0, 0, 0] ,
[0, 0, 0, 0, 0, 0, 0, 0, -73, 0, -90, 0, 0, 96, 0, 150, 0, 0, 0, 0, 0, 0, 0, 0, -24, 0, 0, 0, -60, 0, 0] ,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 105, -114, 0, 28, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -152, 0, 0, 0, 0, 0] ,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 29, 0, 0, 0, 0, 210, 0, 0, 0, 0, 0, 0, 0, 0, 0, -152, 0, 0, -60, 0, 0] ,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -407, 0, 0, 0, -30, 510, 0, 0, 374, 0, 0, -120, 0, 0, 0, 272, 0, 0, 0, 0] ,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -38, 0, -26, 0, 0, 0, -26, 78, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -26] ,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -15, -54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 48, 0, 0, -72, 0, 0, 0] ,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 0, 0, 0, -26, 78, 0, 0, 0, 0, 0, 0, 0, -72, 0, 0, -26] ,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -147, 0, 0, 0, 0, 0, 0, -120, 0, 0, 0, 0, 0, 120, 0, 0] ,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -221, -44, -66, -170, 0, 0, 0, 0, 0, 0, -136, 0, 0, -44, 0] ,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -69, -44, 0, 0, 0, 0, 0, 0, 0, 0, -72, 0, -44, 0] ,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -70, 104, 0, 0, 0, 0, 0, 0, 0, 0, 0, -44, -26] ,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -141, 0, 0, 0, 0, 0, 0, -136, 0, 0, 0, 52] ,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -81, -130, 0, 0, 0, 0, 0, 0, 0, 0, 0] ,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -61, 0, 0, 0, -152, 0, 0, 0, 0, 0] ,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 120, 0, 0, 0, 0, 0, 0, 0, 0] ,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 152, 0, 0, 0, 0, 0] ,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 72, 0, 0, 0] ,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ] )



#CAP= -FL = 4

sampler = EmbeddingComposite(DWaveSampler(solver=dict(topology__type='zephyr')))
sampleset = sampler.sample_qubo(- QUBO_ex15_lambda2, num_reads=5000,  label="Adv2_EX15: 12 nodes, 22 transactions, lambda0=2")
print(sampleset)

'''
sampler = ExactSolver()
sampleset = sampler.sample_qubo(- QUBO_ex7_lambda8)
print(sampleset)
'''

with open('output.txt', mode='w') as file_object:
    for datum in sampleset.data(fields=['sample', 'energy', 'num_occurrences']):
        print("\'",datum,"\', ",file=file_object)



dwave.inspector.show(sampleset)