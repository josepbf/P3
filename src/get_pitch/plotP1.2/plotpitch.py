import matplotlib.pyplot as plt
import numpy as np

res_txt = open("/home/josep/Escritorio/PAV/P3/src/get_pitch/plotP1.2/res.txt","r")
lines = res_txt.readlines()
waveform = []
for x in range(len(lines)-10):
    waveform.append(float(lines[x+10]))

autocorrelation = []
sum = 0
for k in range(300):
    for i in range(len(waveform)-k-1):
        sum = sum + waveform[i]*waveform[i+k]
    autocorrelation.append(sum/(len(waveform)))

plt.figure()

plt.subplot(211)
plt.plot(waveform, 'b')
plt.title('Waveform')
plt.xlabel('n')
plt.xlim([0, len(waveform)])
plt.grid()

plt.subplot(212)
plt.plot(autocorrelation, 'r')
plt.title('Autocorrelation')
plt.xlabel('l')
plt.xlim([0, len(autocorrelation)])
plt.grid()

plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.45,
                    wspace=0.35)

plt.show()