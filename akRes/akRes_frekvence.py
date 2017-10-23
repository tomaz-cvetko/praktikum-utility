A = 0.567
B = 0.385
C = 0.24

c_0 = 340
N = 5

import math

# tabela lastnig \omega za lastna valovanja
lastne_frekvence = []


for nx in range(N):
    for ny in range(N):
        for nz in range(N):
            omega = c_0 * math.pi * math.sqrt((nx/A)**2 + (ny/B)**2 + (nz/C)**2)
            nu = omega/(2*math.pi)
            lastne_frekvence.append((nu, nx, ny, nz, omega))

with open('freqs.dat', 'w') as out:
    print('#Lowest frequencies for the box.', file=out)
    print('#<nx|ny|nz>', file=out)
    for item in sorted(lastne_frekvence, key=lambda x: x[0]):
        print('{0[1]}|{0[2]}|{0[3]} freq: {0[0]:.4f} (omega: {0[4]:.2f})'.format(item), file=out)