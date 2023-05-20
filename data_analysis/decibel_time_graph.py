import matplotlib.pyplot as plt
import numpy as np
import wave

# Open the audio file and extract its properties
audio_file = wave.open(r"C:\Users\Jooney Han\Desktop\과학전람회\충음실 데이터\자름_음원\20안자름.wav", "rb")
sample_rate = audio_file.getframerate()
num_frames = audio_file.getnframes()
duration = num_frames / float(sample_rate)

# Define the start time and end time for plotting
start_time = 1.5  # Modify the start time as desired
end_time = 4

# Calculate the corresponding start and end frame indices
start_frame = int(start_time * sample_rate)
end_frame = int(end_time * sample_rate)

# Read the audio data into a numpy array
audio_data = np.frombuffer(audio_file.readframes(num_frames), dtype=np.int16)

# Convert the amplitude to decibels
amplitude_dB = 20 * np.log10(np.abs(audio_data))

# Calculate the time values corresponding to each sample
time_values = np.linspace(0, duration, num_frames)

# Only include the corresponding values of amplitude_dB within the desired time range
amplitude_dB = amplitude_dB[start_frame:end_frame]
time_values = time_values[start_frame:end_frame]

# Plot the audio signal as a function of time in decibels
plt.plot(time_values, amplitude_dB)
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude (dB)')

# Manipulate x-axis ticks
plt.xticks(np.linspace(start_time, end_time, num=32))
plt.gca().xaxis.set_major_locator(plt.MaxNLocator(32))

plt.show()
