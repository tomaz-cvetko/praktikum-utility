import math
import numpy as np

A = 0.567
B = 0.385
C = 0.24

def hitrost(freq, config):
    return (2*freq)/math.sqrt((config[0]/A)**2 + (config[1]/B)**2 + (config[2]/C)**2)

resonance = [304, 456, 546]
Ns = [(1, 0, 0), (0, 1, 0), (1, 1, 0)]

hitrost = [hitrost(x, y) for x, y in zip(resonance, Ns)]
print(hitrost)

hitrost = np.array(hitrost)
print(np.average(hitrost))
print(np.std(hitrost))

