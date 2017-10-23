import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema

data = np.loadtxt('interval_scan2.dat')

w = np.array([[1, 2, 1, 0],
                  [2, 2, 2, 0],
                  [3, 2, 1, 0],
                  [4, 2, 2, 0],
                  [5, 2, 1, 0]])

y = np.array([[1, 2, 1, 2],
               [2, 2, 0, 0],
               [5, 3, 4, 4]])


# print(argrelextrema.__doc__)

maxima = argrelextrema(data[:,2], np.greater, order=20, axis=0)
#print(maxima[0])

resonance = [data[max, 0] for max in maxima[0]]
odzivi = [data[max, 2] for max in maxima[0]]

for max in zip(resonance, odzivi):
    print(max)

# plt.plot(data[:,0], data[:,1], 'k-', label='max-min U(t)')
plt.title('Resonančni odziv v območju 200Hz - 1000Hz')
plt.xlabel(r'$\nu$ [Hz]')
plt.ylabel(r'$U_{dev}$')


plt.plot(data[:,0], data[:,2], 'k-', label='povprecna U(t)')
plt.plot(resonance[:], odzivi[:], 'r.', label='vrhovi')


plt.rc('font', size=8)

n = 0
for i, j in zip(resonance, odzivi):
    n += 1
    if n > 5:
        break
    elif n == 2:
        continue
    plt.annotate('({:.0f}, {:.3f})'.format(i, j), xy=(i, j), xytext=(-20, 5), textcoords='offset points')

#plt.savefig('scan_graph.png', dpi=600)
plt.show()