import librosa
import numpy as np
import matplotlib.pyplot as plt

def get_pitch_name(pitch_index):
    # Define the mapping between pitch index and musical notes
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

    # Get the note name corresponding to the pitch index
    octave = pitch_index // len(notes)
    note = notes[pitch_index % len(notes)]

    return f'{note}{octave}'

def plot_wav_graph(wav_file, cluster_threshold=5):
    # Load the audio file
    audio_data, sample_rate = librosa.load(wav_file)

    # Compute the pitch using Librosa
    pitches, _ = librosa.piptrack(y=audio_data, sr=sample_rate)

    # Extract the most prominent pitch for each frame
    pitch_values = np.argmax(pitches, axis=0)

    # Create the time axis
    duration = len(audio_data) / sample_rate
    time = np.linspace(0, duration, len(pitch_values))

    # Find the clusters of pitch values
    pitch_diff = np.abs(np.diff(pitch_values))
    cluster_indices = np.where(pitch_diff > cluster_threshold)[0] + 1
    cluster_indices = np.concatenate(([0], cluster_indices, [len(pitch_values) - 1]))

    # Get the representative pitch values for each cluster
    cluster_pitch_values = pitch_values[cluster_indices]

    # Convert pitch index to musical note names
    cluster_pitch_names = [get_pitch_name(pitch_index) for pitch_index in cluster_pitch_values]

    # Plot the graph with clustered pitch values
    plt.plot(time, pitch_values)

    # Set the labels and title
    plt.xlabel('Time (s)')
    plt.ylabel('Pitch')
    plt.title('Pitch Graph')

    # Set the y-tick labels as the pitch names for clustered pitch values
    plt.yticks(cluster_pitch_values, cluster_pitch_names)

    # Display the graph
    plt.show()

# Provide the path to your .wav file
wav_file_path = '옥타브변경.wav'

# Set the cluster threshold (adjust as needed)
cluster_threshold = 5

# Call the function to plot the graph
plot_wav_graph(wav_file_path, cluster_threshold)
