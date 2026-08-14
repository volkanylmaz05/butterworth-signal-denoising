import matplotlib.pyplot as plt #for graph 
import numpy as np #for linspace etc.
from scipy import signal #for signal functions

fs = 500  # Sampling frequency

t = np.arange(0,1,1/fs) # dt=0.002s, 1 second duration

clear_signal = np.sin(2 * np.pi * 5 * t) # 5Hz Frequency

np.random.seed(0) #for similarity in noise generation
noise = 0.5 * np.random.randn(len(t))
noisy_signal = clear_signal + noise

sos = signal.butter(4, 8, fs=fs, btype="low", output="sos") #4th order low-pass Butterworth filter with cutoff frequency of 8Hz = 5*1.6 also low-pass filter is used to remove high-frequency noise from the signal. The cutoff frequency is set to 8Hz, which is higher than the frequency of the clear signal (5Hz) to ensure that the clear signal is preserved while attenuating the noise.
filtered_signal = signal.sosfiltfilt(sos, noisy_signal)

plt.figure(figsize=(12, 8)) # 4:3 aspect ratio for better visualization
plt.subplot(3, 1, 1) #first subplot for clear signal
plt.plot(t, clear_signal)
plt.title("Clear Signal")
plt.ylabel("Amplitude")

plt.subplot(3, 1, 2) #second subplot for noisy signal
plt.plot(t, noisy_signal)
plt.title("Noisy Signal")
plt.ylabel("Amplitude")

plt.subplot(3, 1, 3) #third subplot for filtered signal
plt.plot(t, filtered_signal)
plt.title("Filtered Signal")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

plt.tight_layout() #for better spacing between subplots
plt.show() #for displaying the plots