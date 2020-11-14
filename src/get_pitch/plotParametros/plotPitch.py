import matplotlib.pyplot as plt
import numpy as np

detector_data = open('/home/josep/Escritorio/PAV/P3/src/get_pitch/plotParametros/rl004.f0')
wavesurfer_data = open('src/get_pitch/plotParametros/rl004.f0ref')
detector_rawdata = detector_data.readlines()
wavesurfer_rawdata = wavesurfer_data.readlines()

detector_data = []
wavesurfer_data = []
for x in range(len(wavesurfer_rawdata)):
    detector_data.append(float(detector_rawdata[x].replace("\n","")))
    wavesurfer_data.append(float(wavesurfer_rawdata[x].replace("\n","")))

t = np.arange(0,len(wavesurfer_data)).astype(float)
t = t/2000

plt.figure()

plt.subplot(211)
plt.plot(t, detector_data, 'b')
plt.title('Detector P3')
plt.ylabel('Hz')
plt.xlabel('s')
plt.grid()

plt.subplot(212)
plt.plot(t, wavesurfer_data, 'r')
plt.title('Detector Wavesurfer')
plt.ylabel('Hz')
plt.xlabel('s')
plt.grid()

plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.45,
                    wspace=0.35)

plt.show()