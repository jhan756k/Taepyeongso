import matplotlib.pyplot as plt
import numpy as np
import wave

# Open the audio file and extract its properties
audio_file = wave.open("simple.wav", "rb")
sample_rate = audio_file.getframerate()
num_frames = audio_file.getnframes()
duration = num_frames / float(sample_rate)
time_limit = 0.05

# Read the audio data into a numpy array
audio_data = np.frombuffer(audio_file.readframes(num_frames), dtype=np.int16)

# Convert the amplitude to decibels
amplitude_dB = 20 * np.log10(np.abs(audio_data))

# Calculate the time values corresponding to each sample
time_values = np.linspace(0, time_limit, int(sample_rate * time_limit))

# Only include the corresponding values of amplitude_dB up to 0.1 seconds
amplitude_dB = amplitude_dB[:int(sample_rate * time_limit)]

# Plot the audio signal as a function of time in decibels
plt.plot(time_values, amplitude_dB)
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude (dB)')
plt.show()
