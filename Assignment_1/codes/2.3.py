# Reducing noise in an audio file

import soundfile as sf
from scipy import signal

# Read .wav file 
input_signal, fs = sf.read('Sound_Noise.wav') 

# Sampling frequency of input signal
sampl_freq = fs

# Order of the filter
order = 4   

# Cutoff frquency is 4kHz
cutoff_freq = 4000.0  

# Digital Frequency
Wn = 2 * cutoff_freq / sampl_freq  

# b and a are numerator and denominator polynomials respectively
b, a = signal.butter(order, Wn, 'low') 

# Filter the input signal with butterworth filter
output_signal = signal.filtfilt(b, a, input_signal)

# Write the output signal into .wav file
sf.write('Sound_With_Reduced_Noise.wav', output_signal, fs) 
