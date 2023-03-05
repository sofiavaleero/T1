import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd

#4
x, fm = sf.read('so_cavall.wav')

T = 0.025
L = int(fm * T)
Tm = 1/fm
t = Tm*np.arange(L)
sf.write('so_cavall.wav', x, fm)

plt.figure(3)
plt.plot(t[0:L], x[0:L])
plt.xlabel('t')
plt.title('grafica evolucio temporal')
plt.show()

from numpy.fft import fft
N = 5000
X = fft(x[0:L], N)

k = np.arange(N)
plt.figure(4)
plt.plot(k, X)
plt.title('TF')
plt.show()
