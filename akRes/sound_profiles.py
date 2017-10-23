import numpy as np
import matplotlib.pyplot as plt

files = ['304', '456', '546', '611']

for entry in files[1:2]:
    filename = entry + 'Hz.dat'
    data = np.loadtxt(filename)

    x_dim = np.linspace(2, 53, 52)
    plt.title('{} Hz'.format(entry))
    plt.xlabel(r'$x_{coordinate}$ [cm]')
    plt.ylabel(r'$U_{dev}$')

    plt.plot(x_dim[3:], data[3:, 2], 'k-')
    #plt.plot(x_dim, data[:, 1], 'r-')

    #plt.savefig(entry + 'Hz.png', dpi=600)
    plt.show()