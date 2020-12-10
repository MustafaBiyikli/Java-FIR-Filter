'''
File: coeffs.py
Project: Java-FIR-Filter
File Created: Thursday, 10 December 2020 @ 11:02:41 am
Author: Mustafa Biyikli (biyiklimustafa96@gmail.com)
-----
Last Modified: Thursday, 10 December 2020 @ 11:45:36 am
Modified By: Mustafa Biyikli (biyiklimustafa96@gmail.com>)
-----
License MIT License (http://www.opensource.org/licenses/mit-license.php)
Copyright (c) 2020 Mustafa Biyikli
'''

import numpy as np
import matplotlib.pyplot as plt
# Freq resolution = /\f = Fs / M
Fs = 1000 # Your sampling rate here (Hz)
M = Fs * 2
# Ideal frequency response
f1 = 45 # cutoff (Hz)
f2 = 55 # cutoff (Hz)
X = np.ones(M)
X[int(f1*Fs/M):int(f2*Fs/M)+1] = 0
X[M-int(f2*2):M-int(f1*2)+1] = 0

# convert to time domain, slice, shift to positive time
x = np.fft.ifft(X)
h = np.zeros(M)
h[0:int(M/2)], h[int(M/2):M] = x[int(M/2):M], x[0:int(M/2)]
# window function
h = h * np.hanning(M)
# DC Removal (sharp DC response)
X = np.fft.fft(h)
X[0:int(0.5/Fs*M)] = 0

h = np.real(np.fft.ifft(X)) # coeffs

np.savetxt("coeffs.txt", [h], delimiter=",") # outputs a .txt file of your coeffs
plt.show()