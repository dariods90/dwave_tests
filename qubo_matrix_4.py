import numpy as np
from dimod import ExactSolver
from dwave.system import DWaveSampler, EmbeddingComposite
import dwave.inspector
import pandas as pd
pd.set_option("display.max_rows", 1000000)


# sampleset.first.sample takes the lowest energy sample result, without cutting any data


print("The correct string is unknown")

QUBO_ex10_lambda10 = np.array( [ [454, -150, 0, 0, 0, 0, 0, 150, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 300, 150, -750, 150, -600, 0, 0, 0, 0, 0, -600] ,
[0, -238, 0, 0, 0, 0, 0, 150, 0, -240, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 630, -600, 0, 0, 0, 0, 0, 0] ,
[0, 0, -739, 0, 0, 660, 0, 0, 0, 0, 900, 0, 0, -40, 0, 0, 0, 0, 0, 660, 0, 0, 0, 0, 0, 0, 480, 0, -160, 0, 0, 0] ,
[0, 0, 0, -9, -80, 0, 0, 0, 0, 0, 0, 0, 0, 120, 180, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -160, 0, 0, 0, 0] ,
[0, 0, 0, 0, -28, 0, 0, 0, 0, 0, 0, 0, 80, 0, 0, 0, 0, 0, 0, 60, 80, 0, 0, 0, 0, 0, 0, -160, 0, 0, 0, 0] ,
[0, 0, 0, 0, 0, 1, -120, 0, 0, 0, -300, 0, 0, 0, 0, 0, 0, 0, 0, -300, 0, 0, 0, 0, 0, 0, -240, 0, -160, 0, 0, 0] ,
[0, 0, 0, 0, 0, 0, -149, 0, 0, 0, 0, 0, 0, 0, 0, 0, 270, 540, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -160, 0, 0, 0] ,
[0, 0, 0, 0, 0, 0, 0, 235, -220, -220, 0, 0, 0, 0, 0, 550, 0, 0, 0, 0, 0, 0, 0, 0, -750, -600, 0, 0, 0, -220, 0, 0] ,
[0, 0, 0, 0, 0, 0, 0, 0, -369, -110, 0, 0, 160, 0, 0, 660, 0, 0, 0, 0, 0, 0, -120, 0, 0, 0, 0, 0, 0, -220, 0, 0] ,
[0, 0, 0, 0, 0, 0, 0, 0, 0, -408, 0, 0, 0, 0, 0, 660, 0, 0, 0, 0, 0, 0, 0, 0, 320, 0, 0, 0, 0, -220, 0, 0] ,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 343, -420, 0, 0, 0, 0, -140, 0, 0, -300, 0, -140, 0, 0, 0, 0, -240, 0, 0, 0, -840, 0] ,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 381, 0, 0, 0, 0, 0, 0, 80, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -840, 0] ,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -39, 0, 0, 0, 0, 0, 0, 0, -160, 0, 240, 0, 0, 0, 0, -160, 0, 0, 0, 0] ,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, -90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -160, 0, 0, 0] ,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -139, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -607, 0, 120, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 440, 0, 0] ,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 195, -270, 0, 0, 0, -280, 0, 0, 0, 0, 0, 0, 0, 0, -840, 0] ,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -327, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -107, 0, 140, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -149, 0, 0, 0, 0, 0, 0, -240, 0, 0, 0, 0, 0] ,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 14, 0, 0, 0, 0, 0, 0, -160, 0, 0, 0, 0] ,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 135, -300, 300, 0, 0, 0, 0, 0, 0, -840, -600] ,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -118, 150, 0, 0, 0, 0, 0, 0, 0, -600] ,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 404, 0, 0, 0, 0, 0, 0, 0, -600] ,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 214, -600, 0, 0, 0, 0, 0, 0] ,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 600, 0, 0, 0, 0, 0, 0] ,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 160, 0, 0, 0, 0] ,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 160, 0, 0, 0] ,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 840, 0] ,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 600] ] )

qpu = DWaveSampler(solver={'topology__type': 'zephyr'})

sampler = EmbeddingComposite(DWaveSampler())
sampleset = sampler.sample_qubo(- QUBO_ex10_lambda10, num_reads=100, label="EX10: 16 nodes, 25 transactions, lambda0=10")
print(sampleset)

'''
sampler = ExactSolver()
sampleset = sampler.sample_qubo(- QUBO_ex7_lambda8)
print(sampleset)
'''

with open('output.txt', mode='w') as file_object:
    for datum in sampleset.data(fields=['sample', 'energy', 'num_occurrences']):
        print(datum,file=file_object)


dwave.inspector.show(sampleset)

