from dimod.generators import and_gate
from dwave.system import DWaveSampler, EmbeddingComposite

'''
bqm = and_gate('in1', 'in2', 'out')
sampler = EmbeddingComposite(DWaveSampler())
sampleset = sampler.sample(bqm, num_reads=10)
print(sampleset)
'''

bqm = [[0,1,-2],[0,0,-2],[0,0,3]]

sampler = EmbeddingComposite(DWaveSampler())
sampleset = sampler.sample_qubo(bqm, num_reads=40)
print(sampleset)
print(bqm)