import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema

data = np.loadtxt('interval_scan2.dat')


#tukaj uporabim funkcijo iz scipyjevega paketa da dobim ekstreme 20 reda (da so vecji od 20ih sosedov na obeh straneh)
maxima = argrelextrema(data[:,2], np.greater, order=20, axis=0)
#print(maxima[0])

# max so indeksi maximumov, v resonance shranim frekvence pri katerih se to zgodi
# v odzivi shranim kako visoko gre tam
resonance = [data[max, 0] for max in maxima[0]]
odzivi = [data[max, 2] for max in maxima[0]]

# natisnem, da se da preverit a je delovalo ok
for max in zip(resonance, odzivi):
    print(max)

# naslov in imena osi
plt.title('Resonančni odziv v območju 200Hz - 1000Hz')
plt.xlabel(r'$\nu$ [Hz]')
plt.ylabel(r'$U_{dev}$')


# dejanski graf resonance
plt.plot(data[:,0], data[:,2], 'k-', label='povprecna U(t)')

# rdece pikice na vrhove
plt.plot(resonance[:], odzivi[:], 'r.', label='vrhovi')


# zmanjsam font za napisane koordinate
plt.rc('font', size=8)


n = 0
for i, j in zip(resonance, odzivi):
    n += 1
    if n > 5:
        # visje frekvence me a) ne zanimajo tako zelo b) se ful nabasejo na graf
        break
    elif n == 2:
        # ta frekvenca je oni midget med obema visokima vrhovoma in je fake
        continue
    # ob vrh pripise koordinate spicke
    plt.annotate('({:.0f}, {:.3f})'.format(i, j), xy=(i, j), xytext=(-20, 5), textcoords='offset points')

# shrani samo ko res hoces (aka najprej probaj, potem overwritaj staro sliko)
#plt.savefig('scan_graph.png', dpi=600)
plt.show()