import numpy as np
import sounddevice as sd

#sequence = "ATC"

# Function to generate a sine wave of given frequency and duration
def generate_sine_wave(frequency, duration, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)  # Generate equally spaced points in time
    wave = np.sin(2 * np.pi * frequency * t)  # Generate the sine wave
    return wave

# Function to combine multiple audio waves
def combine_waves(waves):
    return np.concatenate(waves)

# Define the melody notes and their corresponding frequencies
notes = {
    'C': 261.63,
    'D': 293.66,
    'E': 329.63,
    'F': 349.23,
    'G': 392.00,
    'A': 440.00,
    'B': 493.88
}

def sequence_validator(sequence):
    sequence = sequence.upper()

    if sequence[0] == ">":
        sequence = sequence.splitlines()
        sequence = sequence[1:]
        sequence = "".join(sequence).strip()

    else:
        sequence = sequence.splitlines()
        sequence = "".join(sequence).strip()

    return sequence

def is_dna(sequence):
    if set(sequence).issubset({"A", "C", "G", "T"}):
        return True
    else:
        return False

# Converting DNA sequence into melody sequence
def melody_maker(sequence):
    #sequence = sequence.upper()
    melody = []
    for nucleotide in sequence:
        if nucleotide == 'A':
            melody.extend(['C','E','G'])
        elif nucleotide == 'C':
            melody.extend(['E','G','B'])
        elif nucleotide == 'G':
            melody.extend(['F','A','C'])
        elif nucleotide == 'T':
            melody.extend(['D','F','A'])
    return melody

# Generate the melody
def play_melody(melody):
    melody_duration = 0.5  # Duration of each note in seconds
    melody_wave = []
    for note in melody:
        frequency = notes[note]  # Get the frequency of the current note
        note_wave = generate_sine_wave(frequency, melody_duration)  # Generate the sine wave for the note
        melody_wave.append(note_wave)  # Append the note waveform to the melody waveform

    # Combine the individual note waves into one wave
    melody_wave_combined = combine_waves(melody_wave)

    # Scale the data to the range of 16-bit integers
    melody_wave_scaled = np.int16(melody_wave_combined * 32767)

    # Play the melody

    sd.play(melody_wave_scaled, samplerate=44100)
    sd.wait()
