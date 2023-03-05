import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd

#1
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

#2
plt.figure(1)
plt.subplot(211)                             
plt.plot(t[0:Ls], x[0:Ls])  
plt.title('evolucio 5 periodes')              
plt.xlabel('t')                                               
plt.ylabel('x')

from numpy.fft import fft
N = 5000
X = fft(x[0 : Ls], N)
k = np.arange(N)
plt.subplot(212)
plt.plot(k, X)
plt.ylabel('X[k]')
plt.xlabel('k')
plt.title('TF')
plt.show()



