import numpy as np
from dimod import ExactSolver
from dwave.system import DWaveSampler, EmbeddingComposite

print("The correct string is \n1  0  1  0  1  0  1  1  0  0  0 \n")


QUBO_ex1_lambda1 = np.array( [[-53,   0,  24,   0,   0,  24,   0,  50,  80,   0,   0],
 [  0,  10,   0,  14,   0,   0,   0, -14,   0, -56,   0],
 [  0,   0,  38, -56,   0,  -8,   0,   0,   0, -56,   0],
 [  0,   0,   0,  39,   0 ,  0,   0,   0,   0, -56,   0],
 [  0,   0,   0,   0,  56 , 12,  14,   0, -72,   0, -72],
 [  0,   0,   0,   0,   0, -15, -24,   0,  24,   0, -72],
 [  0,   0,   0,   0,   0 ,  0,   9,   0,  24,   0, -72],
 [  0,   0,   0,  0 ,  0 ,  0 ,  0,   7, -50, -56,   0],
 [  0,   0,   0,   0 ,  0 ,  0 ,  0,   0,   0,   0, -72],
 [  0,   0,   0,   0 ,  0 ,  0 ,  0 ,  0,   0,  56,   0],
 [  0,   0,   0,   0 ,  0,   0 ,  0,   0,   0,   0,  72]] )


'''
sampler = ExactSolver()
sampleset = sampler.sample_qubo(-QUBO_ex1_lambda1)
print(sampleset)


sampler = EmbeddingComposite(DWaveSampler())
sampleset = sampler.sample_qubo(- QUBO_ex1_lambda1, num_reads=1000,label="MPBS (ex1) test with 9 transactions")
print(sampleset)
'''


QUBO_ex1_lambda5 = np.array( [[-277,    0,  120,    0,    0,  120,    0,  250,  400,    0,    0],
 [   0,   38,    0,   70,    0,    0,    0,  -70,    0, -280,    0],
 [   0,    0,  174, -280,    0,  -40,    0,    0,    0, -280,    0],
 [   0,    0,    0,  179,    0,    0,    0,    0,    0, -280,    0],
 [   0,    0,    0,    0,  268,   60,   70,    0, -360,    0, -360],
 [   0,    0,    0,    0,    0,  -79, -120,    0,  120,    0, -360],
 [   0,    0,    0,    0,    0,    0,   29,    0,  120,    0, -360],
 [   0,    0,    0,    0,    0,    0,    0,   23, -250, -280,    0],
 [   0,    0,    0,    0,    0,    0,    0,    0,  -16,    0, -360],
 [   0,    0,    0,    0,    0,    0,    0,    0,    0,  280,    0],
 [   0,    0,    0,    0,    0,    0,    0,    0,    0,    0,  360]] )

'''
sampler = ExactSolver()
sampleset = sampler.sample_qubo(-QUBO_ex1_lambda5)
print(sampleset)

sampler = EmbeddingComposite(DWaveSampler())
sampleset = sampler.sample_qubo(- QUBO_ex1_lambda5, num_reads=1000,label="MPBS (ex1) test with 9 transactions (lambda=5)")
print(sampleset)
'''
QUBO_ex1_lambda075=np.array ([[-39.,     0.,    18.,     0.,     0.,    18.,     0.,    37.5,   60.,     0.,   0.,  ],
 [  0.,     8.25,   0.,    10.5,    0.,     0.,     0.,   -10.5,    0.,   -42.,  0.,  ],
 [  0.,     0.,    29.5,  -42.,     0.,    -6.,     0.,     0. ,    0.,   -42.,  0.,  ],
 [  0.,     0.,     0.,    30.25,   0.,     0.,     0.,     0.,     0.,   -42.,  0.,  ],
 [  0.,     0.,     0.,     0.,    42.75,   9.,    10.5,    0.,   -54.,     0., -54.,  ],
 [  0.,     0.,     0.,     0.,     0.,   -11.,   -18.,     0.,    18.,     0., -54.,  ],
 [  0.,     0.,     0.,     0.,     0.,     0.,     7.75,   0.,    18.,     0.,  -54.,  ],
 [  0.,     0.,     0.,     0.,     0.,     0.,     0.,     6.,   -37.5,  -42.,    0.,  ],
 [  0.,     0.,     0.,     0.,     0.,     0.,     0.,     0.,     1.,     0.,  -54.,  ],
 [  0.,     0.,     0.,     0.,     0.,     0.,     0.,     0.,     0.,    42.,    0.,  ],
 [  0.,     0.,     0.,     0.,     0.,     0.,     0.,     0.,     0.,     0.,   54.,  ]] )


'''
sampler = ExactSolver()
sampleset = sampler.sample_qubo(-QUBO_ex1_lambda075)
print(sampleset)
'''
sampler = EmbeddingComposite(DWaveSampler())
sampleset = sampler.sample_qubo(- QUBO_ex1_lambda075,num_reads=1000,label="MPBS (ex1) test with 9 transactions (lambda=075)")
print(sampleset)
