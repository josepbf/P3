import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf

data, samplerate = sf.read('audioSonorode30ms.wav')

autocorrelation = np.correlate(data, data, mode='same')
autocorrelation2 = []
a = int(len(autocorrelation)/2)
for x in range(int(len(autocorrelation)/2-1)):
    autocorrelation2.append(autocorrelation[x+int(len(autocorrelation)/2)-1])

plt.figure()

plt.subplot(211)
plt.plot(data, 'b')
plt.title('Waveform')
plt.xlabel('n')
plt.xlim([0, len(data)])
plt.grid()

plt.subplot(212)
plt.plot(autocorrelation2, 'r')
plt.title('Autocorrelation')
plt.xlabel('l')
plt.xlim([0, len(autocorrelation2)])
plt.grid()

plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.45,
                    wspace=0.35)

plt.show()