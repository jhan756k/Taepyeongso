import librosa
import librosa.display
import matplotlib.pyplot as plt  
import numpy as np

audio = "tp.wav"  
# y, sr = librosa.load(audio, sr=44100) # 모든 데이터 0~1 값으로 정규화
# sin graph
N = 512
T = 1.0 / 44100.0
f1 = 697
f2 = 1209
t = np.linspace(0.0, N*T, N)
y1 = 1.1 * np.sin(2 * np.pi * f1 * t)
y2 = 0.9 * np.sin(2 * np.pi * f2 * t)
y = y1 + y2

# fft
yf = np.fft.fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N//2)

plt.subplot(2, 1, 1)

plt.plot(t, y)
plt.grid()
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplot(2, 1, 2)
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
plt.grid()
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.show()
