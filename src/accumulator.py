import numpy as np

coefficents = np.array([[10,10,10,10],[10,10,10,10]])

data = np.array([[1,1,1,1],[2,2,2,2]])

intermediate = data * coefficents

print(intermediate)

print(np.sum(intermediate,axis=0))