import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd

T= 2.5   
fm=8000                              
fx=4000                              
A=4                                  
pi=np.pi
L = int(fm * T)                   
Tm=1/fm                           
t=Tm*np.arange(L)                 
x = A * np.cos(2 * pi * fx * t)   
sf.write('so_exemple1.wav', x, fm)  
Tx=1/fx    
Ls=int(fm*5*Tx)                      

from numpy.fft import fft
N = 5000
X = fft(x[0 : Ls], N)
k = np.arange(N)


#3

X_db = 20*np.log10(np.abs(X)/max(np.abs(X)))
fk = (k/N)*fm
plt.figure(2)
plt.xlim([0, fm/2])
plt.plot(fk, X_db)
plt.xlabel('f')
plt.ylabel('XdB')
plt.show()