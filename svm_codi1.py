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
x, fm = sf.read('so_exemple1.wav')
sd.play(x, fm)