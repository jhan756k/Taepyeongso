import librosa
import librosa.display
import matplotlib.pyplot as plt  
import numpy as np

audio = "tp.wav"  
y, sr = librosa.load(audio, sr=44100) # 모든 데이터 0~1 값으로 정규화

plt.figure(figsize=(10, 5))
librosa.display.waveshow(y, sr=sr)

fft = np.fft.fft(y)

magnitude = np.abs(fft)
frequency = np.linspace(0, sr, len(magnitude))

left_frequency = frequency[:int(len(frequency)/2)]
left_magnitude = magnitude[:int(len(frequency)/2)]

plt.figure(figsize=(10, 5))
plt.plot(left_frequency, left_magnitude)
plt.xlabel("Frequency")
plt.ylabel("Magnitude")
plt.show()
