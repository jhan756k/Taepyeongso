import wave
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft

# Read the audio file
audio_file = wave.open("simple.wav", "rb")

# Get the number of frames, channels, and sample rate
nframes = audio_file.getnframes()
nchannels = audio_file.getnchannels()
framerate = audio_file.getframerate()

# Read the audio data
audio_data = audio_file.readframes(nframes)

# Convert the audio data to a numpy array
audio_data = np.frombuffer(audio_data, dtype=np.int16)

# Calculate the time array
time_array = np.linspace(0, nframes/framerate, num=len(audio_data))

# Perform the FFT on the audio data
fft_data = fft(audio_data)

# Get the frequency array
freq_array = np.linspace(0, framerate / 2, len(fft_data) // 2)

# Plot the frequency to time graph
plt.plot(time_array, audio_data)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()

plt.plot(freq_array, np.abs(fft_data[:len(fft_data)//2]))
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.show()